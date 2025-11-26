"""
Time-based One-Time Password (TOTP) helper utilities.
"""

from __future__ import annotations

import base64
from io import BytesIO
from typing import Dict, Optional

import pyotp
import qrcode

from config import get_settings


settings = get_settings()
_pending_totp_secrets: Dict[int, str] = {}


def start_totp_setup(user_id: int, username: str) -> tuple[str, str]:
    """
    Generate and store a pending TOTP secret, returning the secret and QR code.

    Args:
        user_id: Authenticated user's ID
        username: Username/email for QR labeling

    Returns:
        Tuple of (secret, base64 PNG QR code string)
    """
    secret = pyotp.random_base32()
    _pending_totp_secrets[user_id] = secret
    uri = pyotp.TOTP(secret).provisioning_uri(
        name=username,
        issuer_name=settings.app_name,
    )
    qr_b64 = _qr_code_base64(uri)
    return secret, qr_b64


def get_pending_secret(user_id: int) -> Optional[str]:
    """Return the pending secret for a user, if any."""
    return _pending_totp_secrets.get(user_id)


def clear_pending_secret(user_id: int) -> None:
    """Remove the pending secret for a user."""
    _pending_totp_secrets.pop(user_id, None)


def verify_totp_code(secret: str, code: str) -> bool:
    """Validate a TOTP code against a secret."""
    totp = pyotp.TOTP(secret)
    return totp.verify(code, valid_window=1)


def _qr_code_base64(data: str) -> str:
    """Render a QR code and return as base64 data URI."""
    img = qrcode.make(data)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    return f"data:image/png;base64,{encoded}"

