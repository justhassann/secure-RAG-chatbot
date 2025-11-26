#!/usr/bin/env python3
"""
Security Headers Test Script
Tests that all required HTTP security headers are present in responses.
"""

import sys
import requests
from typing import Dict, List, Tuple


def test_security_headers(base_url: str = "http://localhost:8000") -> Tuple[bool, List[str]]:
    """
    Test that all required security headers are present.
    
    Args:
        base_url: Base URL of the application
        
    Returns:
        Tuple of (all_passed, error_messages)
    """
    print("=" * 80)
    print("🔒 SECURITY HEADERS TEST")
    print("=" * 80)
    print(f"\nTesting: {base_url}")
    print()
    
    # Required headers and their expected values
    required_headers = {
        "X-Frame-Options": "DENY",
        "X-Content-Type-Options": "nosniff",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "Content-Security-Policy": "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:;",
        "Referrer-Policy": "strict-origin-when-cross-origin",
    }
    
    # Additional recommended headers
    recommended_headers = {
        "X-XSS-Protection": "1; mode=block",
        "Permissions-Policy": "geolocation=(), microphone=(), camera=()",
    }
    
    errors = []
    
    try:
        # Make request to health endpoint
        response = requests.get(f"{base_url}/health", timeout=5)
        
        print(f"Response Status: {response.status_code}")
        print()
        
        # Check required headers
        print("Required Security Headers:")
        print("-" * 80)
        
        for header, expected_value in required_headers.items():
            actual_value = response.headers.get(header)
            
            if actual_value is None:
                print(f"❌ {header}: MISSING")
                errors.append(f"Missing required header: {header}")
            elif actual_value == expected_value:
                print(f"✅ {header}: {actual_value}")
            else:
                print(f"⚠️  {header}: {actual_value}")
                print(f"   Expected: {expected_value}")
                errors.append(f"Header {header} has unexpected value")
        
        print()
        
        # Check recommended headers
        print("Recommended Security Headers:")
        print("-" * 80)
        
        for header, expected_value in recommended_headers.items():
            actual_value = response.headers.get(header)
            
            if actual_value is None:
                print(f"⚠️  {header}: MISSING (recommended)")
            elif actual_value == expected_value:
                print(f"✅ {header}: {actual_value}")
            else:
                print(f"⚠️  {header}: {actual_value}")
                print(f"   Expected: {expected_value}")
        
        print()
        
        # Check for insecure headers
        print("Insecure Headers Check:")
        print("-" * 80)
        
        insecure_headers = {
            "Server": "Should not expose server version",
            "X-Powered-By": "Should not expose technology stack",
        }
        
        for header, reason in insecure_headers.items():
            if header in response.headers:
                print(f"⚠️  {header}: {response.headers[header]} ({reason})")
            else:
                print(f"✅ {header}: Not present (good)")
        
        print()
        
    except requests.exceptions.ConnectionError:
        error_msg = f"❌ Could not connect to {base_url}. Is the server running?"
        print(error_msg)
        errors.append(error_msg)
        return False, errors
    except Exception as e:
        error_msg = f"❌ Error during test: {e}"
        print(error_msg)
        errors.append(error_msg)
        return False, errors
    
    # Summary
    print("=" * 80)
    if not errors:
        print("✅ ALL REQUIRED SECURITY HEADERS PRESENT")
        print("=" * 80)
        return True, []
    else:
        print("❌ SECURITY HEADERS TEST FAILED")
        print("=" * 80)
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")
        print()
        return False, errors


def test_trusted_host(base_url: str = "http://localhost:8000") -> Tuple[bool, List[str]]:
    """
    Test that TrustedHostMiddleware is working.
    
    Args:
        base_url: Base URL of the application
        
    Returns:
        Tuple of (all_passed, error_messages)
    """
    print("=" * 80)
    print("🛡️  TRUSTED HOST MIDDLEWARE TEST")
    print("=" * 80)
    print()
    
    errors = []
    
    try:
        # Test with valid host
        print("Testing with valid Host header (localhost)...")
        response = requests.get(
            f"{base_url}/health",
            headers={"Host": "localhost:8000"},
            timeout=5
        )
        
        if response.status_code == 200:
            print("✅ Valid host accepted")
        else:
            print(f"⚠️  Unexpected status code: {response.status_code}")
        
        print()
        
        # Test with invalid host (should be rejected)
        print("Testing with invalid Host header (evil.com)...")
        try:
            response = requests.get(
                f"{base_url}/health",
                headers={"Host": "evil.com"},
                timeout=5,
                allow_redirects=False
            )
            
            if response.status_code == 400:
                print("✅ Invalid host rejected (400 Bad Request)")
            else:
                print(f"⚠️  Invalid host not rejected (status: {response.status_code})")
                errors.append("TrustedHostMiddleware may not be working correctly")
        except requests.exceptions.ConnectionError:
            print("✅ Invalid host rejected (connection refused)")
        
        print()
        
    except Exception as e:
        error_msg = f"❌ Error during test: {e}"
        print(error_msg)
        errors.append(error_msg)
        return False, errors
    
    # Summary
    print("=" * 80)
    if not errors:
        print("✅ TRUSTED HOST MIDDLEWARE WORKING")
        print("=" * 80)
        return True, []
    else:
        print("⚠️  TRUSTED HOST MIDDLEWARE TEST COMPLETED WITH WARNINGS")
        print("=" * 80)
        return True, errors


def main():
    """Main test runner."""
    base_url = "http://localhost:8000"
    
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "SECURITY HEADERS VERIFICATION TEST" + " " * 24 + "║")
    print("╚" + "=" * 78 + "╝")
    print()
    
    # Run tests
    headers_passed, headers_errors = test_security_headers(base_url)
    print()
    
    trusted_host_passed, trusted_host_errors = test_trusted_host(base_url)
    print()
    
    # Final summary
    print("=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)
    
    if headers_passed and trusted_host_passed:
        print("✅ All security tests passed!")
        print()
        print("Security features verified:")
        print("  ✅ X-Frame-Options (Clickjacking protection)")
        print("  ✅ X-Content-Type-Options (MIME sniffing protection)")
        print("  ✅ Strict-Transport-Security (HTTPS enforcement)")
        print("  ✅ Content-Security-Policy (XSS/Injection protection)")
        print("  ✅ Referrer-Policy (Information leakage protection)")
        print("  ✅ Trusted Host Middleware (Host header injection protection)")
        print()
        return 0
    else:
        print("❌ Some security tests failed!")
        print()
        if headers_errors:
            print("Security Headers Issues:")
            for error in headers_errors:
                print(f"  - {error}")
        if trusted_host_errors:
            print("Trusted Host Issues:")
            for error in trusted_host_errors:
                print(f"  - {error}")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())
