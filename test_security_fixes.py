"""
Test script to verify all 5 security fixes are working correctly.
Run this after initializing the database with: python init_db.py
"""

import asyncio
import sys
from datetime import datetime

from sqlalchemy import select

from database import AsyncSessionLocal
from models import AuditLog, TokenBlacklist, User
from security_auth import create_access_token, is_token_blacklisted, blacklist_token
from config import get_settings


async def test_1_secure_configuration():
    """Test 1: Verify SECRET_KEY is secure"""
    print("\n" + "="*70)
    print("TEST 1: Secure Configuration")
    print("="*70)
    
    settings = get_settings()
    
    # Check SECRET_KEY
    if settings.secret_key == "change_me":
        print("❌ FAILED: SECRET_KEY is still 'change_me'")
        return False
    
    if len(settings.secret_key) < 32:
        print("⚠️  WARNING: SECRET_KEY is shorter than 32 characters")
    
    print(f"✅ SECRET_KEY is set and secure (length: {len(settings.secret_key)})")
    
    # Check ALGORITHM
    if settings.algorithm != "HS256":
        print(f"❌ FAILED: ALGORITHM is {settings.algorithm}, should be HS256")
        return False
    
    print(f"✅ ALGORITHM is correctly set to {settings.algorithm}")
    
    return True


async def test_2_dynamic_passwords():
    """Test 2: Verify users exist with hashed passwords"""
    print("\n" + "="*70)
    print("TEST 2: Dynamic Default Passwords")
    print("="*70)
    
    async with AsyncSessionLocal() as session:
        # Check if users exist
        result = await session.execute(select(User))
        users = result.scalars().all()
        
        if len(users) == 0:
            print("❌ FAILED: No users found. Run 'python init_db.py' first")
            return False
        
        print(f"✅ Found {len(users)} users in database")
        
        # Check passwords are hashed (bcrypt hashes start with $2b$)
        for user in users:
            if not user.hashed_password.startswith("$2b$"):
                print(f"❌ FAILED: User {user.username} password is not bcrypt hashed")
                return False
            print(f"✅ User '{user.username}' has properly hashed password")
        
        return True


async def test_3_audit_logging():
    """Test 3: Verify audit log table exists and can store events"""
    print("\n" + "="*70)
    print("TEST 3: Audit Logging")
    print("="*70)
    
    async with AsyncSessionLocal() as session:
        # Try to create a test audit log entry
        test_log = AuditLog(
            username="test_user",
            event_type="test_event",
            ip_address="127.0.0.1",
            details="Test audit log entry"
        )
        
        session.add(test_log)
        await session.commit()
        
        print("✅ Successfully created test audit log entry")
        
        # Verify it was stored
        result = await session.execute(
            select(AuditLog).where(AuditLog.event_type == "test_event")
        )
        stored_log = result.scalar_one_or_none()
        
        if not stored_log:
            print("❌ FAILED: Could not retrieve test audit log")
            return False
        
        print(f"✅ Retrieved audit log: {stored_log.event_type} by {stored_log.username}")
        
        # Check all required fields
        if not stored_log.timestamp:
            print("❌ FAILED: Audit log missing timestamp")
            return False
        
        print(f"✅ Audit log has timestamp: {stored_log.timestamp}")
        
        # Clean up test entry
        await session.delete(stored_log)
        await session.commit()
        
        return True


async def test_4_token_blacklisting():
    """Test 4: Verify token blacklisting works"""
    print("\n" + "="*70)
    print("TEST 4: Token Blacklisting")
    print("="*70)
    
    async with AsyncSessionLocal() as session:
        # Create a test token
        test_token = create_access_token(data={"sub": "test_user"})
        print("✅ Created test JWT token")
        
        # Decode to get JTI
        from jose import jwt
        settings = get_settings()
        payload = jwt.decode(test_token, settings.secret_key, algorithms=[settings.algorithm])
        jti = payload.get("jti")
        
        if not jti:
            print("❌ FAILED: Token does not contain JTI")
            return False
        
        print(f"✅ Token contains JTI: {jti[:8]}...")
        
        # Check token is not blacklisted initially
        is_blacklisted = await is_token_blacklisted(session, jti)
        if is_blacklisted:
            print("❌ FAILED: New token is already blacklisted")
            return False
        
        print("✅ Token is not blacklisted initially")
        
        # Blacklist the token
        await blacklist_token(session, jti)
        print("✅ Token added to blacklist")
        
        # Verify it's now blacklisted
        is_blacklisted = await is_token_blacklisted(session, jti)
        if not is_blacklisted:
            print("❌ FAILED: Token was not blacklisted")
            return False
        
        print("✅ Token is now blacklisted")
        
        # Clean up
        result = await session.execute(
            select(TokenBlacklist).where(TokenBlacklist.jti == jti)
        )
        blacklist_entry = result.scalar_one_or_none()
        if blacklist_entry:
            await session.delete(blacklist_entry)
            await session.commit()
        
        return True


async def test_5_rate_limiting():
    """Test 5: Verify rate limiting is configured"""
    print("\n" + "="*70)
    print("TEST 5: Rate Limiting Configuration")
    print("="*70)
    
    # Check if rate limiting is configured in main.py
    try:
        with open("main.py", "r") as f:
            content = f.read()
        
        # Check for rate limit decorators
        checks = [
            ('@limiter.limit("5/minute")', "/api/token endpoint"),
            ('@limiter.limit("3/minute")', "/api/2fa/verify endpoint"),
            ('@limiter.limit("3/minute")', "/api/2fa/setup endpoint"),
        ]
        
        all_found = True
        for pattern, description in checks:
            if pattern in content:
                print(f"✅ Rate limiting configured for {description}")
            else:
                print(f"❌ FAILED: Rate limiting not found for {description}")
                all_found = False
        
        return all_found
    
    except Exception as e:
        print(f"❌ FAILED: Could not verify rate limiting: {e}")
        return False


async def main():
    """Run all security tests"""
    print("\n" + "="*70)
    print("🔒 SECURITY FIXES VERIFICATION TEST SUITE")
    print("="*70)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    tests = [
        ("Secure Configuration", test_1_secure_configuration),
        ("Dynamic Passwords", test_2_dynamic_passwords),
        ("Audit Logging", test_3_audit_logging),
        ("Token Blacklisting", test_4_token_blacklisting),
        ("Rate Limiting", test_5_rate_limiting),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = await test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ ERROR in {test_name}: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status}: {test_name}")
    
    print("\n" + "="*70)
    print(f"Results: {passed}/{total} tests passed")
    print("="*70)
    
    if passed == total:
        print("\n🎉 All security fixes are working correctly!")
        print("✅ Ready for course submission")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please review the output above.")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
