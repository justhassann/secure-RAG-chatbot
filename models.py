"""
Database ORM models.
"""

from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import TypeDecorator

from database import Base


class EncryptedString(TypeDecorator):
    """
    SQLAlchemy type decorator for encrypting string columns at rest.
    Uses Fernet symmetric encryption with a key derived from SECRET_KEY.
    """
    impl = String
    cache_ok = True
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fernet = None
    
    def _get_fernet(self):
        """Lazy load Fernet cipher to avoid circular imports."""
        if self._fernet is None:
            from cryptography.fernet import Fernet
            from config import get_settings
            import base64
            import hashlib
            
            settings = get_settings()
            # Derive a 32-byte key from SECRET_KEY for Fernet
            key = base64.urlsafe_b64encode(
                hashlib.sha256(settings.secret_key.encode()).digest()
            )
            self._fernet = Fernet(key)
        return self._fernet
    
    def process_bind_param(self, value, dialect):
        """Encrypt value before storing in database."""
        if value is None:
            return None
        fernet = self._get_fernet()
        encrypted = fernet.encrypt(value.encode())
        return encrypted.decode('utf-8')
    
    def process_result_value(self, value, dialect):
        """Decrypt value when reading from database."""
        if value is None:
            return None
        fernet = self._get_fernet()
        decrypted = fernet.decrypt(value.encode())
        return decrypted.decode('utf-8')


class User(Base):
    """Application user with RBAC-related metadata."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    email: Mapped[Optional[str]] = mapped_column(String(255), unique=True, nullable=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False, default="Staff")
    department: Mapped[str] = mapped_column(String(50), nullable=False, default="general")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    totp_secret: Mapped[Optional[str]] = mapped_column(
        EncryptedString(255),  # Encrypted at rest
        nullable=True
    )


class AuditLog(Base):
    """Audit log for tracking security events and user actions."""

    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.utcnow, 
        nullable=False,
        index=True
    )
    username: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, index=True)
    event_type: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    ip_address: Mapped[Optional[str]] = mapped_column(String(45), nullable=True)
    details: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


class TokenBlacklist(Base):
    """Blacklist for revoked JWT tokens (logout functionality)."""

    __tablename__ = "token_blacklist"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    jti: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    revoked_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.utcnow, 
        nullable=False
    )

