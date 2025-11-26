"""
Initialize the SQLite database and seed default users.
"""

import asyncio
import secrets
from typing import Dict, List

from sqlalchemy import select

from database import Base, AsyncSessionLocal, engine
from models import User
from security_auth import get_password_hash


# Default user templates (passwords will be generated dynamically)
DEFAULT_USER_TEMPLATES = [
    {
        "username": "admin",
        "email": "admin@example.com",
        "role": "Executive",
        "department": "it",
    },
    {
        "username": "alice",
        "email": "alice@example.com",
        "role": "Staff",
        "department": "hr",
    },
    {
        "username": "bob",
        "email": "bob@example.com",
        "role": "SecurityAnalyst",
        "department": "security",
    },
]


async def create_tables() -> None:
    """Create database tables."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def seed_users() -> Dict[str, str]:
    """
    Insert default users if they do not already exist.
    Returns a dictionary of username:password for newly created users.
    """
    created_users: Dict[str, str] = {}
    
    async with AsyncSessionLocal() as session:
        for user_template in DEFAULT_USER_TEMPLATES:
            result = await session.execute(
                select(User).where(User.username == user_template["username"])
            )
            existing = result.scalar_one_or_none()
            
            if existing:
                continue

            # Generate a strong random password
            generated_password = secrets.token_urlsafe(12)
            
            user = User(
                username=user_template["username"],
                email=user_template["email"],
                hashed_password=get_password_hash(generated_password),
                role=user_template["role"],
                department=user_template["department"],
                is_active=True,
                totp_secret=None,
            )
            session.add(user)
            created_users[user.username] = generated_password

        await session.commit()

    return created_users


async def main():
    print("=" * 70)
    print("🔧 Initializing database...")
    print("=" * 70)
    
    await create_tables()
    print("✅ Database tables created successfully.")
    
    created = await seed_users()
    
    if created:
        print("\n" + "=" * 70)
        print("🔐 DEFAULT USER CREDENTIALS (SAVE THESE SECURELY!)")
        print("=" * 70)
        print("\n⚠️  These passwords are randomly generated and will NOT be shown again!")
        print("⚠️  Copy them now before closing this window!\n")
        
        for username, password in created.items():
            print(f"  Username: {username}")
            print(f"  Password: {password}")
            print()
        
        print("=" * 70)
        print("✅ Default users created successfully.")
        print("=" * 70)
    else:
        print("\n✅ Default users already exist. No new users created.")
        print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())

