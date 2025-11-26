"""
Test RBAC implementation for RAG system
"""

from rbac import get_allowed_departments, get_role_description, check_access

print("=" * 70)
print("RBAC Policy Testing")
print("=" * 70)

test_cases = [
    ("Intern", "it", "IT Intern - should only see IT + general"),
    ("Staff", "hr", "HR Staff - should only see HR + general"),
    ("HR_Officer", "hr", "HR Officer - fixed to HR + general"),
    ("Finance_Officer", "finance", "Finance Officer - fixed to finance + general"),
    ("TeamLead", "security", "Security Team Lead - own dept + general"),
    ("Manager", "it", "IT Manager - own dept + general + hr + finance"),
    ("SecurityAnalyst", "security", "Security Analyst - security + it + general"),
    ("SysAdmin", "it", "SysAdmin - all departments"),
    ("Auditor", "compliance", "Auditor - all departments"),
    ("Executive", "executive", "Executive - all departments"),
]

print("\n")
for role, dept, description in test_cases:
    allowed = get_allowed_departments(role, dept)
    desc = get_role_description(role)
    
    print(f"📋 {description}")
    print(f"   Role: {role}, Department: {dept}")
    print(f"   Allowed: {', '.join(allowed)}")
    print(f"   Description: {desc}")
    print()

# Test specific access checks
print("=" * 70)
print("Access Check Examples")
print("=" * 70)
print()

access_tests = [
    ("Intern", "it", "hr", False, "IT Intern trying to access HR docs"),
    ("Intern", "it", "it", True, "IT Intern accessing IT docs"),
    ("Manager", "finance", "hr", True, "Finance Manager accessing HR docs"),
    ("SecurityAnalyst", "security", "finance", False, "Security Analyst trying to access Finance"),
    ("SysAdmin", "it", "finance", True, "SysAdmin accessing any department"),
]

for role, dept, target, expected, description in access_tests:
    has_access = check_access(role, dept, target)
    status = "✅ PASS" if has_access == expected else "❌ FAIL"
    result = "CAN" if has_access else "CANNOT"
    
    print(f"{status} {description}")
    print(f"      {role} ({dept}) {result} access {target}")
    print()

print("=" * 70)
print("RBAC Testing Complete!")
print("=" * 70)
