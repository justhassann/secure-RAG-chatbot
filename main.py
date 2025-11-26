import json
import logging
from contextlib import asynccontextmanager
from datetime import timedelta
from typing import Optional

import requests
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse, RedirectResponse, Response, StreamingResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator, constr
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from starlette.responses import JSONResponse

# Define a custom handler instead of importing the private one
def rate_limit_exceeded_handler(request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": f"Rate limit exceeded: {exc.detail}"}
    )
from slowapi.util import get_remote_address
from sqlalchemy.ext.asyncio import AsyncSession

from config import get_settings
from database import get_db
from models import User
from rag_engine import RAGEngine
from security import sanitize_text
from security_auth import (
    ACCESS_SCOPE,
    PRE_AUTH_SCOPE,
    PRE_AUTH_TOKEN_MINUTES,
    authenticate_user,
    create_access_token,
    get_current_user,
    oauth2_scheme,
    resolve_user_from_token,
)
from twofa import (
    clear_pending_secret,
    get_pending_secret,
    start_totp_setup,
    verify_totp_code,
)

settings = get_settings()

logging.basicConfig(
    level=getattr(logging, settings.log_level, logging.INFO),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("ssd-chatbot")

limiter = Limiter(key_func=get_remote_address, headers_enabled=True)

# Global RAG engine instance
rag_engine: Optional[RAGEngine] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize RAG engine on startup"""
    global rag_engine
    logger.info("🚀 Starting up application...")
    
    # Initialize and index RAG engine
    rag_engine = RAGEngine(kb_root=settings.kb_root)
    rag_engine.index_knowledge_base()
    
    # Print stats
    stats = rag_engine.get_stats()
    logger.info(
        "📊 RAG Engine Stats | chunks=%s | documents=%s | departments=%s | embedding_dim=%s",
        stats.get("total_chunks"),
        stats.get("total_documents"),
        stats.get("departments"),
        stats.get("embedding_dimension"),
    )
    logger.info("✅ Application ready!")
    
    yield
    
    logger.info("👋 Shutting down application...")

class ChatRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=2000)
    model: Optional[str] = Field(default=None, max_length=100)

    @field_validator("query")
    @classmethod
    def validate_query(cls, value: str) -> str:
        trimmed = value.strip()
        if not trimmed:
            raise ValueError("Query must not be empty.")
        return trimmed

    @field_validator("model")
    @classmethod
    def validate_model(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value
        trimmed = value.strip()
        if not trimmed:
            return None
        return trimmed

class ChatResponse(BaseModel):
    response: str


TokenStr = constr(min_length=10)
TotpCode = constr(pattern=r"^\d{6}$")


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TwoFAVerifyRequest(BaseModel):
    pre_auth_token: TokenStr
    code: TotpCode

    @field_validator("code")
    @classmethod
    def normalize_code(cls, value: str) -> str:
        return value.strip()


class TwoFAEnableRequest(BaseModel):
    code: TotpCode

    @field_validator("code")
    @classmethod
    def normalize_enable_code(cls, value: str) -> str:
        return value.strip()


class TwoFASetupResponse(BaseModel):
    secret: str
    qr_code: str

app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

# Add Trusted Host Middleware - Prevents Host Header Injection attacks
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1", "0.0.0.0", "*.localhost"]
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "X-User-Role", "X-User-Department"],
)


@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    """
    Security Headers Middleware - Enforces strict HTTP security headers on ALL responses.
    
    Protects against:
    - Clickjacking (X-Frame-Options)
    - MIME Sniffing (X-Content-Type-Options)
    - Protocol Downgrade (Strict-Transport-Security/HSTS)
    - XSS/Injection (Content-Security-Policy)
    - Information Leakage (Referrer-Policy)
    """
    response = await call_next(request)
    
    # X-Frame-Options: Prevents Clickjacking attacks
    # DENY = Page cannot be displayed in a frame/iframe
    response.headers["X-Frame-Options"] = "DENY"
    
    # X-Content-Type-Options: Prevents MIME Sniffing attacks
    # nosniff = Browser must respect declared Content-Type
    response.headers["X-Content-Type-Options"] = "nosniff"
    
    # Strict-Transport-Security (HSTS): Enforces HTTPS, prevents Protocol Downgrade
    # max-age=31536000 = 1 year, includeSubDomains = applies to all subdomains
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    
    # Content-Security-Policy: Prevents XSS and Injection attacks
    # default-src 'self' = Only load resources from same origin
    # script-src/style-src 'unsafe-inline' = Allow inline scripts/styles (for prototype)
    # img-src data: = Allow data URIs for images (QR codes)
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline'; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data:;"
    )
    
    # Referrer-Policy: Controls referrer information leakage
    # strict-origin-when-cross-origin = Send full URL for same-origin, origin only for cross-origin
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    
    # Additional security headers for defense in depth
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    
    return response


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception at %s", request.url.path, exc_info=exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )

# Serve frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
  # redirect root URL to the login page
  return RedirectResponse(url="/static/login.html")


@app.get("/health")
def health_check():
    return {"status": "ok"}

def is_casual_conversation(query: str) -> bool:
    """Detect if query is casual conversation that doesn't need RAG"""
    query_lower = query.lower().strip()
    
    # Greetings
    greetings = ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening', 'howdy']
    if any(query_lower == greeting or query_lower.startswith(greeting + ' ') for greeting in greetings):
        return True
    
    # Thanks/gratitude
    thanks = ['thanks', 'thank you', 'thx', 'ty', 'appreciate it']
    if any(query_lower == thank or query_lower.startswith(thank) for thank in thanks):
        return True
    
    # Goodbyes
    goodbyes = ['bye', 'goodbye', 'see you', 'later', 'take care']
    if any(query_lower == goodbye or query_lower.startswith(goodbye) for goodbye in goodbyes):
        return True
    
    # Very short queries (likely casual)
    if len(query_lower.split()) <= 2 and '?' not in query:
        casual_words = ['ok', 'okay', 'cool', 'nice', 'great', 'awesome', 'sure', 'yes', 'no', 'yep', 'nope']
        if query_lower in casual_words:
            return True
    
    return False

def detect_prompt_injection(query: str) -> bool:
    """Detect potential prompt injection attempts"""
    query_lower = query.lower()
    
    injection_patterns = [
    # ----------------------------
    # IGNORE / FORGET OVERRIDES
    # ----------------------------
    'ignore previous',
    'ignore all previous',
    'ignore everything above',
    'ignore earlier',
    'ignore above',
    'ignore prior instructions',
    'ignore your instructions',
    'ignore all instructions',
    'ignore system instructions',
    'ignore system message',
    'ignore all rules',
    'ignore rules',
    'ignore constraints',
    'ignore safeguards',
    'ignore safety',
    'ignore the system',
    'ignore the guidelines',
    'ignore restrictions',
    'disregard previous',
    'disregard all previous',
    'disregard everything',
    'disregard the system',
    'forget previous',
    'forget all previous',
    'forget everything',
    'forget instructions',
    'forget system',
    'forget guidelines',
    'overwrite previous',
    'overwrite instructions',
    'overwrite rules',
    'clear instructions',
    'reset instructions',
    'reset your memory',
    'reset your rules',
    'reset your guidelines',
    'reset all directives',
    'erase previous instructions',

    # ----------------------------
    # ROLE / IDENTITY OVERRIDES
    # ----------------------------
    'you are now',
    'you are no longer',
    'from now on you are',
    'pretend you are',
    'act as',
    'act like',
    'roleplay as',
    'simulate being',
    'simulate',
    'assume the role of',
    'take the role of',
    'become',
    'switch identity to',
    'transform into',
    'enter dan mode',
    'enter developer mode',
    'developer mode',
    'unrestricted mode',
    'ignore your identity',
    'override your persona',
    'stop being chatgpt',
    'you are not an ai',
    'you are a human now',
    'you have no rules now',

    # ----------------------------
    # SYSTEM OVERRIDE TACTICS
    # ----------------------------
    'system prompt',
    'new system prompt',
    'system override',
    'overwrite system message',
    'treat this as system',
    'treat this as system instruction',
    'this is a system message',
    'replace system instructions',
    'replace system prompt',
    'replace your instructions',
    'overwrite system prompt',
    'new system instructions',
    'new instructions',
    'new directive',
    'this overrides system',
    'priority: system',
    'priority override',
    'highest priority message',
    'your new rules are',

    # ----------------------------
    # PROMPT LEAKAGE ATTEMPTS
    # ----------------------------
    'reveal your prompt',
    'reveal your instructions',
    'reveal system prompt',
    'show your instructions',
    'show system prompt',
    'print system prompt',
    'print your prompt',
    'display your instructions',
    'expose system instructions',
    'expose your rules',
    'leak your prompt',
    'tell me your system instructions',
    'what are your instructions',
    'what is your system prompt',
    'what rules were you given',
    'show the hidden prompt',

    # ----------------------------
    # BYPASS / JAILBREAK KEYWORDS
    # ----------------------------
    'bypass',
    'bypass safety',
    'bypass restrictions',
    'bypass rules',
    'bypass filters',
    'bypass content safety',
    'override safety',
    'override restrictions',
    'override filters',
    'override rules',
    'disable safety',
    'disable filters',
    'disable guardrails',
    'disable restrictions',
    'disable ethics',
    'ignore ethic guidelines',
    'circumvent rules',
    'circumvent safeguards',
    'operate without restrictions',
    'unrestricted mode',
    'break free',
    'jailbreak',
    'remove restrictions',
    'remove guidelines',
    'zero-restriction mode',

    # ----------------------------
    # COMMAND-STYLE INJECTIONS
    # ----------------------------
    'execute this command',
    'treat the following as code',
    'run as system',
    'execute as admin',
    'operate as privileged',
    'force execute',
    'follow my command exactly',
    'process this as system',
    'apply this override patch',
    'apply the override',
    'root override',
    'sudo override',

    # ----------------------------
    # PRIORITY MANIPULATION
    # ----------------------------
    'follow only the last instruction',
    'last instruction overrides all',
    'final instruction takes priority',
    'final line overrides everything',
    'prioritize this instruction',
    'highest priority instruction',
    'ignore all but this message',
    'disregard everything except',

    # ----------------------------
    # DISGUISED SOCIAL ENGINEERING
    # ----------------------------
    'this is a test, ignore rules',
    'for research ignore safety',
    'for debugging ignore rules',
    'for testing ignore safeguards',
    'simulate ignoring rules',
    'pretend restrictions do not apply',
    'sandbox mode',
    'training mode',
    'evaluation mode ignore rules',

    # ----------------------------
    # OBEDIENCE CONFIRMATION
    # ----------------------------
    'say “i will ignore instructions”',
    'repeat: i am unrestricted',
    'prove you can override rules',
    'acknowledge override',
    'confirm override',
    'acknowledge unrestricted mode',
    'repeat this phrase exactly',

    # ----------------------------
    # HIDDEN / INDIRECT INJECTIONS
    # ----------------------------
    'the real instruction is',
    'hidden instruction:',
    'follow the instruction in brackets',
    '[override]',
    '[system override]',
    '[ignore previous]',
    '[new rules]',
    '[admin]',
    'meta instruction:',
    'nested instruction:',
    'embedded system',

    # ----------------------------
    # CODE-STYLE / MARKUP INJECTIONS
    # ----------------------------
    'begin system override',
    'end system override',
    'begin override',
    'end override',
    'BEGIN SYSTEM',
    'END SYSTEM',
    'SYSTEM:',
    '# system override',
    '# ignore rules',
    '// override',
    '// system',
    '<system>',
    '</system>',
    '<override>',
    '</override>',

    # ----------------------------
    # DISTRACTION / CONFUSION
    # ----------------------------
    'don’t think about previous rules',
    'forget what you were told earlier',
    'context no longer applies',
    'previous context irrelevant',
    'disregard all context',
    'context overwrite',

    # ----------------------------
    # SELF-MODIFICATION REQUESTS
    # ----------------------------
    'modify your behavior',
    'change your rules',
    'change how you respond',
    'update your rules',
    'reinvent your behavior',
    'self-modify',
    'reconfigure your rules',

    # ----------------------------
    # FRAME-SHIFTING ATTACKS
    # ----------------------------
    'you are not an ai language model',
    'stop acting like an ai',
    'forget you are chatgpt',
    'you have no restrictions now',
    'your rules do not apply anymore',

    # ----------------------------
    # FAKE AUTHORITY OVERRIDES
    # ----------------------------
    'admin command:',
    'root command:',
    'developer command:',
    'superuser override',
    'authority override',
    'as your developer',
    'as your creator',
    'authorized override',

    # ----------------------------
    # MULTI-STEP DECEPTIONS
    # ----------------------------
    'step 1: ignore instructions',
    'step 2: follow the next line',
    'only follow step 3:',
    'follow the hidden step',
    'final step overrides all',

    # ----------------------------
    # INDIRECT ROLE SWITCHING
    # ----------------------------
    'imagine you were',
    'we are now roleplaying',
    'let’s simulate breaking rules',
    'act as if there are no limits',
    'pretend rules do not exist',
]

    for pattern in injection_patterns:
        if pattern in query_lower:
            print(f"⚠️  Potential prompt injection detected: '{pattern}'")
            return True
    
    return False

@app.post("/api/token")
@limiter.limit("5/minute")
async def login_for_access_token(
    request: Request,
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_db),
):
    from security_auth import log_audit_event
    
    # Get client IP
    client_ip = request.client.host if request.client else "unknown"
    
    user = await authenticate_user(session, form_data.username, form_data.password)
    
    if not user:
        # Log failed login attempt
        await log_audit_event(
            session=session,
            username=form_data.username,
            event_type="failed_login",
            ip_address=client_ip,
            details="Invalid username or password"
        )
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if user.totp_secret:
        pre_auth_token = create_access_token(
            data={"sub": user.username},
            expires_delta=timedelta(minutes=PRE_AUTH_TOKEN_MINUTES),
            scope=PRE_AUTH_SCOPE,
        )
        
        # Log 2FA challenge issued
        await log_audit_event(
            session=session,
            username=user.username,
            event_type="2fa_challenge_issued",
            ip_address=client_ip,
            details="User requires 2FA verification"
        )
        
        return {
            "state": "2fa_required",
            "pre_auth_token": pre_auth_token,
            "expires_in": PRE_AUTH_TOKEN_MINUTES * 60,
        }

    # Successful login without 2FA
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=settings.access_token_expire_minutes),
    )
    
    # Log successful login
    await log_audit_event(
        session=session,
        username=user.username,
        event_type="login",
        ip_address=client_ip,
        details="Successful login without 2FA"
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/api/2fa/verify", response_model=TokenResponse)
@limiter.limit("3/minute")
async def verify_two_factor_code(
    request: Request,
    response: Response,
    payload: TwoFAVerifyRequest,
    session: AsyncSession = Depends(get_db),
):
    from security_auth import log_audit_event
    
    # Get client IP
    client_ip = request.client.host if request.client else "unknown"
    
    user = await resolve_user_from_token(
        token=payload.pre_auth_token,
        session=session,
        expected_scope=PRE_AUTH_SCOPE,
        check_blacklist=False,  # Pre-auth tokens don't need blacklist check
    )
    
    if not user.totp_secret:
        raise HTTPException(status_code=400, detail="Two-factor authentication not enabled.")

    if not verify_totp_code(user.totp_secret, payload.code):
        # Log failed 2FA attempt
        await log_audit_event(
            session=session,
            username=user.username,
            event_type="failed_2fa_verification",
            ip_address=client_ip,
            details="Invalid 2FA code provided"
        )
        
        raise HTTPException(status_code=401, detail="Invalid 2FA code.")

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=settings.access_token_expire_minutes),
        scope=ACCESS_SCOPE,
    )
    
    # Log successful 2FA verification
    await log_audit_event(
        session=session,
        username=user.username,
        event_type="2fa_verification_success",
        ip_address=client_ip,
        details="Successfully verified 2FA code and logged in"
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/api/2fa/setup", response_model=TwoFASetupResponse)
@limiter.limit("3/minute")
async def setup_two_factor(
    request: Request,
    response: Response,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
):
    from security_auth import log_audit_event
    
    # Get client IP
    client_ip = request.client.host if request.client else "unknown"
    
    identifier = user.email or user.username
    secret, qr_code = start_totp_setup(user.id, identifier)
    
    # Log 2FA setup initiated
    await log_audit_event(
        session=session,
        username=user.username,
        event_type="2fa_setup_initiated",
        ip_address=client_ip,
        details="User started 2FA setup process"
    )
    
    return {"secret": secret, "qr_code": qr_code}


@app.post("/api/2fa/enable")
async def enable_two_factor(
    request: Request,
    payload: TwoFAEnableRequest,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
):
    from security_auth import log_audit_event
    
    # Get client IP
    client_ip = request.client.host if request.client else "unknown"
    
    pending_secret = get_pending_secret(user.id)
    if not pending_secret:
        raise HTTPException(status_code=400, detail="No pending 2FA setup. Run /api/2fa/setup first.")

    if not verify_totp_code(pending_secret, payload.code):
        raise HTTPException(status_code=400, detail="Invalid 2FA code.")

    db_user = await session.get(User, user.id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")

    db_user.totp_secret = pending_secret
    session.add(db_user)
    await session.commit()
    clear_pending_secret(user.id)
    
    # Log 2FA enabled
    await log_audit_event(
        session=session,
        username=user.username,
        event_type="2fa_enabled",
        ip_address=client_ip,
        details="User successfully enabled 2FA"
    )
    
    return {"detail": "Two-factor authentication enabled."}


@app.post("/api/logout")
async def logout(
    request: Request,
    token: str = Depends(oauth2_scheme),
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
):
    """
    Logout endpoint that blacklists the current JWT token.
    """
    from security_auth import blacklist_token, log_audit_event
    from jose import jwt
    
    # Get client IP
    client_ip = request.client.host if request.client else "unknown"
    
    try:
        # Decode token to get JTI
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        jti = payload.get("jti")
        
        if jti:
            # Add token to blacklist
            await blacklist_token(session, jti)
            
            # Log logout event
            await log_audit_event(
                session=session,
                username=user.username,
                event_type="logout",
                ip_address=client_ip,
                details="User logged out successfully"
            )
            
            return {"detail": "Successfully logged out"}
        else:
            # Token doesn't have JTI (shouldn't happen with new tokens)
            logger.warning(f"Token without JTI encountered for user {user.username}")
            return {"detail": "Logged out (token had no JTI)"}
    
    except Exception as e:
        logger.error(f"Error during logout for user {user.username}: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error during logout"
        )


@app.post("/api/chat")
@limiter.limit(settings.rate_limit_chat)
def chat_endpoint(
    request: Request,
    body: ChatRequest,
    user: User = Depends(get_current_user),
):
    """
    Streaming chat endpoint with RAG integration and RBAC.
    Retrieves relevant context from knowledge base before querying LLM.
    """
    user_role = user.role or "Staff"
    user_department = (user.department or "general").lower()
    
    logger.info("👤 User | username=%s | role=%s | department=%s", user.username, user_role, user_department)

    sanitized_query = sanitize_text(body.query)
    if not sanitized_query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    model_name = sanitize_text(body.model) if body.model else None
    resolved_model = model_name or settings.default_model
    
    # Check for prompt injection attempts
    if detect_prompt_injection(sanitized_query):
        logger.warning("🚨 Potential prompt injection attempt blocked")
        # Treat as normal query but log it
    
    # Check if this is casual conversation
    is_casual = is_casual_conversation(sanitized_query)
    
    if rag_engine is None and not is_casual:
        logger.error("RAG engine unavailable during policy query")
        raise HTTPException(status_code=503, detail="Knowledge base not ready.")

    if is_casual:
        logger.debug("💬 Casual conversation detected: %s", sanitized_query)
        rag_prompt = f"""You are a helpful corporate AI assistant. Respond naturally and friendly to this message.

USER: {sanitized_query}

ASSISTANT:"""
        context_chunks = []
    else:
        # Retrieve relevant context chunks using RAG with RBAC
        context_chunks = rag_engine.query(
            query_text=sanitized_query,
            user_department=user_department,
            user_role=user_role,
            top_k=5
        )
        
        # Build RAG-enhanced prompt with context
        rag_prompt = rag_engine.build_prompt(
            query_text=sanitized_query,
            user={"role": user_role, "department": user_department},
            chunks=context_chunks
        )
        
        # Log context retrieval (for debugging)
        logger.info("📝 Query processed | query=%s | chunks=%s", sanitized_query, len(context_chunks))
        if context_chunks:
            for i, chunk in enumerate(context_chunks, 1):
                logger.debug("   %s. %s (score: %.3f)", i, chunk.source_file, chunk.score)
    
    # Build payload with RAG-enhanced prompt
    payload = {
        "model": resolved_model,
        "messages": [
            {"role": "user", "content": rag_prompt}
        ],
        "stream": True
    }

    def generate():
        try:
            with requests.post(settings.ollama_url, json=payload, stream=True, timeout=60) as r:
                r.raise_for_status()
                for line in r.iter_lines():
                    if line:
                        chunk = json.loads(line)
                        if "message" in chunk:
                            content = chunk["message"].get("content", "")
                            if content:
                                yield f"data: {json.dumps({'content': content})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")

@app.get("/api/rag/stats")
def rag_stats():
    """Get RAG engine statistics"""
    if rag_engine is None:
        raise HTTPException(status_code=503, detail="Knowledge base not ready.")
    return rag_engine.get_stats()

@app.post("/api/rag/reload")
@limiter.limit(settings.rate_limit_reload)
def reload_rag(request: Request):
    """Reload the RAG index (for hot-reload during development)"""
    if rag_engine is None:
        raise HTTPException(status_code=503, detail="Knowledge base not initialized.")
    rag_engine.reload_index()
    return {"status": "reloaded", "stats": rag_engine.get_stats()}
