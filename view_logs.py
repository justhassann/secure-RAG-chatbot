"""
Utility script to view audit logs and blacklisted tokens from the database.
Usage: python view_logs.py [options]
"""

import asyncio
import sys
from datetime import datetime
from typing import Optional

from sqlalchemy import select, func

from database import AsyncSessionLocal
from models import AuditLog, TokenBlacklist


async def view_audit_logs(limit: int = 10, event_type: Optional[str] = None, username: Optional[str] = None):
    """View audit logs with optional filtering."""
    print("\n" + "="*80)
    print("📋 AUDIT LOGS")
    print("="*80)
    
    async with AsyncSessionLocal() as session:
        query = select(AuditLog)
        
        # Apply filters
        if event_type:
            query = query.where(AuditLog.event_type == event_type)
        if username:
            query = query.where(AuditLog.username == username)
        
        # Order by most recent first
        query = query.order_by(AuditLog.timestamp.desc()).limit(limit)
        
        result = await session.execute(query)
        logs = result.scalars().all()
        
        if not logs:
            print("\n❌ No audit logs found.")
            if event_type or username:
                print(f"   Filters: event_type={event_type}, username={username}")
            return
        
        print(f"\nShowing {len(logs)} most recent logs:")
        if event_type:
            print(f"Filtered by event_type: {event_type}")
        if username:
            print(f"Filtered by username: {username}")
        print()
        
        # Print header
        print(f"{'ID':<6} {'Timestamp':<20} {'Username':<15} {'Event Type':<25} {'IP Address':<15}")
        print("-" * 80)
        
        # Print logs
        for log in logs:
            timestamp_str = log.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            username_str = log.username or "N/A"
            ip_str = log.ip_address or "N/A"
            
            print(f"{log.id:<6} {timestamp_str:<20} {username_str:<15} {log.event_type:<25} {ip_str:<15}")
            
            if log.details:
                print(f"       Details: {log.details}")
        
        print()


async def view_audit_stats():
    """View statistics about audit logs."""
    print("\n" + "="*80)
    print("📊 AUDIT LOG STATISTICS")
    print("="*80)
    
    async with AsyncSessionLocal() as session:
        # Total logs
        total_result = await session.execute(select(func.count(AuditLog.id)))
        total = total_result.scalar()
        
        print(f"\nTotal audit log entries: {total}")
        
        if total == 0:
            print("No audit logs found.")
            return
        
        # Count by event type
        print("\nEvents by type:")
        event_types = [
            "login",
            "failed_login",
            "logout",
            "2fa_challenge_issued",
            "2fa_verification_success",
            "failed_2fa_verification",
            "2fa_setup_initiated",
            "2fa_enabled",
        ]
        
        for event_type in event_types:
            count_result = await session.execute(
                select(func.count(AuditLog.id)).where(AuditLog.event_type == event_type)
            )
            count = count_result.scalar()
            if count > 0:
                print(f"  {event_type:<30} {count:>5}")
        
        # Most active users
        print("\nMost active users (top 5):")
        user_counts = await session.execute(
            select(AuditLog.username, func.count(AuditLog.id).label('count'))
            .where(AuditLog.username.isnot(None))
            .group_by(AuditLog.username)
            .order_by(func.count(AuditLog.id).desc())
            .limit(5)
        )
        
        for username, count in user_counts:
            print(f"  {username:<20} {count:>5} events")
        
        # Recent activity (last hour)
        from datetime import timedelta
        one_hour_ago = datetime.utcnow() - timedelta(hours=1)
        recent_result = await session.execute(
            select(func.count(AuditLog.id)).where(AuditLog.timestamp >= one_hour_ago)
        )
        recent_count = recent_result.scalar()
        print(f"\nActivity in last hour: {recent_count} events")
        
        print()


async def view_blacklisted_tokens(limit: int = 10):
    """View blacklisted tokens."""
    print("\n" + "="*80)
    print("🚫 BLACKLISTED TOKENS")
    print("="*80)
    
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(TokenBlacklist)
            .order_by(TokenBlacklist.revoked_at.desc())
            .limit(limit)
        )
        tokens = result.scalars().all()
        
        if not tokens:
            print("\n✅ No blacklisted tokens found.")
            return
        
        print(f"\nShowing {len(tokens)} most recently blacklisted tokens:\n")
        
        # Print header
        print(f"{'ID':<6} {'JTI (Token ID)':<40} {'Revoked At':<20}")
        print("-" * 80)
        
        # Print tokens
        for token in tokens:
            revoked_str = token.revoked_at.strftime("%Y-%m-%d %H:%M:%S")
            jti_short = token.jti[:36] + "..." if len(token.jti) > 36 else token.jti
            print(f"{token.id:<6} {jti_short:<40} {revoked_str:<20}")
        
        # Count total
        count_result = await session.execute(select(func.count(TokenBlacklist.id)))
        total = count_result.scalar()
        print(f"\nTotal blacklisted tokens: {total}")
        print()


async def view_failed_logins(limit: int = 10):
    """View failed login attempts."""
    print("\n" + "="*80)
    print("⚠️  FAILED LOGIN ATTEMPTS")
    print("="*80)
    
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(AuditLog)
            .where(AuditLog.event_type.in_(["failed_login", "failed_2fa_verification"]))
            .order_by(AuditLog.timestamp.desc())
            .limit(limit)
        )
        logs = result.scalars().all()
        
        if not logs:
            print("\n✅ No failed login attempts found.")
            return
        
        print(f"\nShowing {len(logs)} most recent failed attempts:\n")
        
        # Print header
        print(f"{'Timestamp':<20} {'Username':<15} {'Type':<25} {'IP Address':<15}")
        print("-" * 80)
        
        # Print logs
        for log in logs:
            timestamp_str = log.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            username_str = log.username or "N/A"
            ip_str = log.ip_address or "N/A"
            
            print(f"{timestamp_str:<20} {username_str:<15} {log.event_type:<25} {ip_str:<15}")
            if log.details:
                print(f"  Details: {log.details}")
        
        print()


async def view_user_activity(username: str):
    """View all activity for a specific user."""
    print("\n" + "="*80)
    print(f"👤 USER ACTIVITY: {username}")
    print("="*80)
    
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(AuditLog)
            .where(AuditLog.username == username)
            .order_by(AuditLog.timestamp.desc())
        )
        logs = result.scalars().all()
        
        if not logs:
            print(f"\n❌ No activity found for user: {username}")
            return
        
        print(f"\nTotal events: {len(logs)}\n")
        
        # Print header
        print(f"{'Timestamp':<20} {'Event Type':<30} {'IP Address':<15}")
        print("-" * 80)
        
        # Print logs
        for log in logs:
            timestamp_str = log.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            ip_str = log.ip_address or "N/A"
            
            print(f"{timestamp_str:<20} {log.event_type:<30} {ip_str:<15}")
            if log.details:
                print(f"  Details: {log.details}")
        
        print()


def print_usage():
    """Print usage information."""
    print("""
Usage: python view_logs.py [command] [options]

Commands:
  logs              View recent audit logs (default)
  stats             View audit log statistics
  blacklist         View blacklisted tokens
  failed            View failed login attempts
  user <username>   View activity for specific user

Options:
  --limit N         Limit number of results (default: 10)
  --event TYPE      Filter by event type
  --username USER   Filter by username

Examples:
  python view_logs.py                          # View recent logs
  python view_logs.py stats                    # View statistics
  python view_logs.py blacklist                # View blacklisted tokens
  python view_logs.py failed                   # View failed logins
  python view_logs.py user admin               # View admin's activity
  python view_logs.py logs --limit 20          # View 20 recent logs
  python view_logs.py logs --event login       # View only login events
  python view_logs.py logs --username alice    # View alice's logs
""")


async def main():
    """Main entry point."""
    args = sys.argv[1:]
    
    if not args or args[0] in ["-h", "--help", "help"]:
        print_usage()
        return
    
    command = args[0]
    
    # Parse options
    limit = 10
    event_type = None
    username = None
    
    i = 1
    while i < len(args):
        if args[i] == "--limit" and i + 1 < len(args):
            limit = int(args[i + 1])
            i += 2
        elif args[i] == "--event" and i + 1 < len(args):
            event_type = args[i + 1]
            i += 2
        elif args[i] == "--username" and i + 1 < len(args):
            username = args[i + 1]
            i += 2
        else:
            i += 1
    
    # Execute command
    try:
        if command == "logs":
            await view_audit_logs(limit=limit, event_type=event_type, username=username)
        elif command == "stats":
            await view_audit_stats()
        elif command == "blacklist":
            await view_blacklisted_tokens(limit=limit)
        elif command == "failed":
            await view_failed_logins(limit=limit)
        elif command == "user" and len(args) > 1:
            target_username = args[1]
            await view_user_activity(target_username)
        else:
            print(f"❌ Unknown command: {command}")
            print_usage()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
