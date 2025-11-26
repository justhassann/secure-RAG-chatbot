"""
Application configuration utilities powered by Pydantic BaseSettings.
Loads values from environment variables / `.env` and exposes a cached accessor.
"""

import logging
import secrets
from functools import lru_cache
from typing import List

from dotenv import load_dotenv
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


load_dotenv()

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """Centralized application configuration."""

    app_name: str = Field(
        default="Secure Corporate Chatbot with RAG",
        alias="APP_NAME",
    )
    ollama_url: str = Field(
        default="http://localhost:11434/api/chat",
        alias="OLLAMA_URL",
    )
    default_model: str = Field(
        default="llama3.1",
        alias="MODEL_NAME",
    )
    kb_root: str = Field(
        default="knowledge_base",
        alias="KB_ROOT",
    )
    allowed_origins: List[str] = Field(
        default_factory=lambda: ["http://localhost:8000"],
        alias="ALLOWED_ORIGINS",
    )
    rate_limit_chat: str = Field(
        default="5/minute",
        alias="RATE_LIMIT_CHAT",
    )
    rate_limit_reload: str = Field(
        default="5/minute",
        alias="RATE_LIMIT_RAG_RELOAD",
    )
    hsts_max_age: int = Field(
        default=31_536_000,
        alias="HSTS_MAX_AGE",
    )
    csp_policy: str = Field(
        default=(
            "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data:; connect-src 'self'; font-src 'self'; frame-ancestors 'none'"
        ),
        alias="CONTENT_SECURITY_POLICY",
    )
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    secret_key: str = Field(default="change_me", alias="SECRET_KEY")
    algorithm: str = Field(default="HS256", alias="ALGORITHM")
    access_token_expire_minutes: int = Field(
        default=30,
        alias="ACCESS_TOKEN_EXPIRE_MINUTES",
    )
    database_url: str = Field(
        default="sqlite+aiosqlite:///./app.db",
        alias="DATABASE_URL",
    )

    @field_validator("secret_key", mode="after")
    @classmethod
    def validate_secret_key(cls, value: str) -> str:
        """
        Validate and auto-generate SECRET_KEY if insecure.
        If SECRET_KEY is 'change_me' or missing, generate a strong random key.
        """
        if not value or value == "change_me":
            generated_key = secrets.token_urlsafe(32)
            logger.warning(
                "⚠️  SECRET_KEY was not set or was insecure. "
                "Auto-generated a secure key for this session. "
                "For production, set SECRET_KEY in your .env file!"
            )
            logger.warning(f"Generated SECRET_KEY: {generated_key}")
            return generated_key
        
        # Warn if key seems too short
        if len(value) < 32:
            logger.warning(
                "⚠️  SECRET_KEY is shorter than recommended (32+ characters). "
                "Consider using a stronger key for production."
            )
        
        return value

    @field_validator("algorithm", mode="after")
    @classmethod
    def validate_algorithm(cls, value: str) -> str:
        """Ensure algorithm is HS256 for security."""
        if value != "HS256":
            logger.warning(
                f"⚠️  ALGORITHM was set to '{value}'. Forcing HS256 for security."
            )
            return "HS256"
        return value

    @field_validator("allowed_origins", mode="before")
    @classmethod
    def _split_origins(cls, value):  # type: ignore[no-untyped-def]
        if not value:
            return ["http://localhost:8000"]
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        return value

    @field_validator("log_level", mode="before")
    @classmethod
    def _normalize_log_level(cls, value: str) -> str:
        return (value or "INFO").upper()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()

