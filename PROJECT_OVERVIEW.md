# Corporate Chatbot with RAG - Project Overview

## Quick Summary

A secure corporate AI chatbot with Role-Based Access Control (RBAC) and Retrieval-Augmented Generation (RAG) for department-specific knowledge base access.

**Security Rating: 6.5/10** (Fair - Good foundation but needs critical fixes)

---

## Core Features

### 1. Authentication System
- JWT-based authentication with 30-minute token expiration
- Two-Factor Authentication (TOTP) support
- Bcrypt password hashing
- Pre-authentication flow for 2FA

### 2. RAG Engine
- Semantic search using sentence-transformers
- PDF and TXT document parsing
- Department-based document filtering
- Context-aware prompt construction
- Prompt injection detection (100+ patterns)

### 3. Role-Based Access Control
**8 Roles:** Intern, Staff, HR_Officer, Finance_Officer, TeamLead, Manager, SecurityAnalyst, SysAdmin, Auditor, Executive

**5 Departments:** HR, IT, Finance, Security, General

**Access Examples:**
- Staff: Own department + general
- Manager: Own department + general + HR + finance
- Executive: All departments

### 4. Technology Stack
- **Backend:** FastAPI, SQLAlchemy, SQLite, Ollama LLM
- **Frontend:** Vanilla JavaScript, HTML5, CSS3
- **AI:** sentence-transformers, PyPDF2, llama3.1
- **Security:** python-jose, passlib, pyotp, bleach
- **Infrastructure:** Docker, Docker Compose

---

## Security Implementation

### ✅ What's Good
- JWT authentication with expiration
- 2FA/TOTP support
- RBAC with department filtering
- Input sanitization (bleach)
- Password hashing (bcrypt)
- Security headers (HSTS, CSP, X-Frame-Options)
- Rate limiting (5 req/min on chat)
- Prompt injection detection

### ❌ Critical Issues
1. **Hardcoded SECRET_KEY** ("change_me")
2. **No HTTPS** (HTTP only in Docker)
3. **Weak default passwords** (AdminPass123!)
4. **SQLite database** (not production-ready)
5. **JWT in localStorage** (XSS vulnerable)
6. **No audit logging**
7. **No CSRF protection**

---

## Quick Start

```bash
# Start everything
docker-compose up -d

# Access at http://localhost:8000

# Default logins:
# admin / AdminPass123!
# alice / AlicePass123!
# bob / BobPass123!
```

---

## Immediate Security Fixes Needed

### Before Production (Critical):
1. Generate strong SECRET_KEY: `openssl rand -hex 32`
2. Enable HTTPS with valid certificates
3. Change all default passwords
4. Migrate from SQLite to PostgreSQL
5. Move JWT from localStorage to httpOnly cookies

### Within 2 Weeks (High):
6. Implement audit logging
7. Add CSRF protection
8. Rate limit all auth endpoints
9. Add account lockout (5 failed attempts)
10. Set up security monitoring

---

## File Structure

```
├── main.py              # FastAPI application & endpoints
├── security_auth.py     # JWT & authentication
├── rbac.py             # Role-based access control
├── rag_engine.py       # RAG retrieval system
├── models.py           # Database models
├── database.py         # SQLAlchemy setup
├── twofa.py            # TOTP 2FA implementation
├── init_db.py          # Database initialization
├── init_kb.py          # Knowledge base setup
├── docker-compose.yml  # Docker orchestration
├── Dockerfile          # Container definition
└── static/             # Frontend files
    ├── login.html
    ├── app.html
    └── *.js
```

---

## API Endpoints

### Authentication
- `POST /api/token` - Login (returns JWT or 2FA challenge)
- `POST /api/2fa/verify` - Verify 2FA code
- `POST /api/2fa/setup` - Start 2FA setup
- `POST /api/2fa/enable` - Enable 2FA

### Chat
- `POST /api/chat` - Send message (streaming response)
- `GET /api/rag/stats` - Knowledge base statistics
- `POST /api/rag/reload` - Reload knowledge base

### Health
- `GET /health` - Health check
- `GET /` - Redirect to login

---

## RBAC Access Matrix

| Role | HR | IT | Finance | Security | General |
|------|----|----|---------|----------|---------|
| Intern | Own | Own | Own | Own | ✓ |
| Staff | Own | Own | Own | Own | ✓ |
| HR_Officer | ✓ | ✗ | ✗ | ✗ | ✓ |
| Finance_Officer | ✗ | ✗ | ✓ | ✗ | ✓ |
| TeamLead | Own | Own | Own | Own | ✓ |
| Manager | ✓ | Own | ✓ | Own | ✓ |
| SecurityAnalyst | ✗ | ✓ | ✗ | ✓ | ✓ |
| SysAdmin/Auditor/Executive | ✓ | ✓ | ✓ | ✓ | ✓ |

*"Own" means their assigned department*

---

## Knowledge Base Structure

```
knowledge_base/
├── hr/
│   ├── employee_handbook.txt
│   ├── leave_policy.txt
│   ├── benefits_guide.txt
│   └── ...
├── it/
│   ├── acceptable_use_policy.txt
│   ├── security_policy.txt
│   └── ...
├── finance/
│   ├── expense_guidelines.txt
│   ├── budget_approval.txt
│   └── ...
├── security/
│   └── ...
└── general/
    └── ...
```

---

## Performance Characteristics

- **Embedding Model:** all-MiniLM-L6-v2 (384 dimensions)
- **Chunk Size:** ~500 characters per paragraph
- **Retrieval:** Top-5 chunks (cosine similarity + keyword overlap)
- **Response Time:** 2-5 seconds (depends on LLM)
- **Memory Usage:** ~500MB (embeddings in RAM)

---

## Deployment Considerations

### Development
- SQLite database
- HTTP only
- Debug logging
- Default credentials

### Production (Recommended)
- PostgreSQL with replication
- HTTPS with valid certificates
- Centralized logging (ELK/Splunk)
- Strong secrets from vault
- Rate limiting per IP
- WAF (Web Application Firewall)
- Monitoring & alerting
- Backup & disaster recovery

---

## Next Steps

1. **Read:** `SECURITY_AUDIT_REPORT.md` for detailed analysis
2. **Fix:** Critical vulnerabilities (SECRET_KEY, HTTPS, passwords)
3. **Test:** Run security tests before production
4. **Deploy:** Use production-grade infrastructure
5. **Monitor:** Set up logging and alerting

---

## Support & Documentation

- Security Audit: `SECURITY_AUDIT_REPORT.md`
- Docker Guide: `README.docker.md`
- RAG Implementation: `RAG_IMPLEMENTATION.md`
- RBAC Status: `RBAC_STATUS.md`

**Last Updated:** November 25, 2025
