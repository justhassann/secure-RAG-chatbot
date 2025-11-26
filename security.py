"""
Security-related helpers including input sanitization and header normalization.
"""

import re
from typing import Optional

import bleach


_ALLOWED_TAGS: list[str] = []
_ALLOWED_ATTRIBUTES: dict[str, list[str]] = {}


def sanitize_text(text: Optional[str]) -> str:
    """
    Remove HTML tags / scripts from user-supplied text and trim whitespace.

    Args:
        text: Raw user input (may be None)

    Returns:
        Sanitized string safe for downstream processing.
    """
    if not isinstance(text, str):
        return ""
    cleaned = bleach.clean(
        text,
        tags=_ALLOWED_TAGS,
        attributes=_ALLOWED_ATTRIBUTES,
        strip=True,
    )
    return cleaned.strip()


def sanitize_header_value(value: Optional[str], default: str) -> str:
    """
    Sanitize header-based metadata such as roles/departments.

    Args:
        value: Header value from the request
        default: Fallback if value is empty after sanitization

    Returns:
        Cleaned string containing safe characters only.
    """
    cleaned = sanitize_text(value)
    if not cleaned:
        return default
    clean_chars = re.sub(r"[^a-zA-Z0-9_\\- ]", "", cleaned)
    return clean_chars or default

