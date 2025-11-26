"""
Authentication helpers: password hashing, JWT creation, 2FA token scopes, and user dependencies.
"""

import uuid
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from jose.exceptions import ExpiredSignatureError
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config import get_settings
from database import get_db
from models import AuditLog, TokenBlacklist, User


settings = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

ACCESS_SCOPE = "access"
PRE_AUTH_SCOPE = "preauth"
PRE_AUTH_TOKEN_MINUTES = 5


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Return True if the provided password matches the stored hash."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash plain text password using bcrypt."""
    return pwd_context.hash(password)


async def log_audit_event(
    session: AsyncSession,
    username: Optional[str],
    event_type: str,
    ip_address: Optional[str],
    details: Optional[str] = None,
) -> None:
    """
    Log an audit event to the database.
    
    Args:
        session: Database session
        username: Username associated with the event (can be None for failed logins)
        event_type: Type of event (e.g., "login", "failed_login", "logout", "2fa_setup")
        ip_address: IP address of the client
        details: Additional details about the event
    """
    audit_log = AuditLog(
        username=username,
        event_type=event_type,
        ip_address=ip_address,
        details=details,
    )
    session.add(audit_log)
    await session.commit()


async def authenticate_user(session: AsyncSession, username: str, password: str) -> Optional[User]:
    """Validate user credentials."""
    result = await session.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    if not user.is_active:
        return None
    return user


def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None,
    scope: str = ACCESS_SCOPE,
) -> str:
    """
    Create a signed JWT token with a unique JTI (JWT ID) for blacklisting support.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.access_token_expire_minutes)
    )
    
    # Add unique JTI for token blacklisting
    jti = str(uuid.uuid4())
    
    to_encode.update({
        "exp": expire,
        "scope": scope,
        "jti": jti,
    })
    
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


async def is_token_blacklisted(session: AsyncSession, jti: str) -> bool:
    """Check if a token JTI is in the blacklist."""
    result = await session.execute(
        select(TokenBlacklist).where(TokenBlacklist.jti == jti)
    )
    return result.scalar_one_or_none() is not None


async def blacklist_token(session: AsyncSession, jti: str) -> None:
    """Add a token JTI to the blacklist."""
    blacklist_entry = TokenBlacklist(jti=jti)
    session.add(blacklist_entry)
    await session.commit()


async def resolve_user_from_token(
    token: str,
    session: AsyncSession,
    expected_scope: str = ACCESS_SCOPE,
    check_blacklist: bool = True,
) -> User:
    """
    Decode a JWT, validate scope, check blacklist, and load the referenced user.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        username: Optional[str] = payload.get("sub")
        token_scope: str = payload.get("scope", ACCESS_SCOPE)
        jti: Optional[str] = payload.get("jti")
        
        if username is None or token_scope != expected_scope:
            raise credentials_exception
        
        # Check if token is blacklisted (only for access tokens)
        if check_blacklist and jti and expected_scope == ACCESS_SCOPE:
            if await is_token_blacklisted(session, jti):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token has been revoked",
                    headers={"WWW-Authenticate": "Bearer"},
                )
    
    except ExpiredSignatureError as exc:
        detail = "2FA token expired" if expected_scope == PRE_AUTH_SCOPE else "Token expired"
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
    except JWTError as exc:
        raise credentials_exception from exc

    result = await session.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()
    if user is None or not user.is_active:
        raise credentials_exception

    return user


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_db),
) -> User:
    """Retrieve the authenticated user from a standard access token."""
    return await resolve_user_from_token(token, session, expected_scope=ACCESS_SCOPE)

