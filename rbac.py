"""
Role-Based Access Control (RBAC) for RAG Document Access

Defines which departments each role can access in the knowledge base.
"""

from typing import List, Dict

# Role-based access policies
ROLE_POLICIES: Dict[str, Dict] = {
    # Basic staff and interns - only their department + general
    "Intern": {
        "inherit_own_department": True,
        "extra_departments": ["general"],
    },
    "Staff": {
        "inherit_own_department": True,
        "extra_departments": ["general"],
    },
    
    # Department-specific officers - fixed departments only
    "HR_Officer": {
        "inherit_own_department": False,
        "fixed_departments": ["hr", "general"],
    },
    "Finance_Officer": {
        "inherit_own_department": False,
        "fixed_departments": ["finance", "general"],
    },
    
    # Leads and managers - own department + some cross-department access
    "TeamLead": {
        "inherit_own_department": True,
        "extra_departments": ["general"],
    },
    "Manager": {
        "inherit_own_department": True,
        "extra_departments": ["general", "hr", "finance"],
    },
    
    # Security-focused roles - security + IT + general
    "SecurityAnalyst": {
        "inherit_own_department": False,
        "fixed_departments": ["security", "it", "general"],
    },
    
    # High-privilege roles - access to everything
    "SysAdmin": {
        "all_departments": True,
    },
    "Auditor": {
        "all_departments": True,
    },
    "Executive": {
        "all_departments": True,
    },
}

# All valid departments in the knowledge base
ALL_DEPARTMENTS = ["hr", "it", "finance", "security", "general"]


def get_allowed_departments(user_role: str, user_department: str) -> List[str]:
    """
    Returns a list of department keys the user is allowed to access,
    based on their role and home department.
    
    Args:
        user_role: User's role (e.g., "Staff", "Manager", "SysAdmin")
        user_department: User's home department (e.g., "hr", "it", "finance")
        
    Returns:
        List of allowed department names
        
    Examples:
        >>> get_allowed_departments("Intern", "it")
        ['it', 'general']
        
        >>> get_allowed_departments("SysAdmin", "it")
        ['hr', 'it', 'finance', 'security', 'general']
        
        >>> get_allowed_departments("HR_Officer", "hr")
        ['hr', 'general']
    """
    # Normalize inputs
    user_role = user_role or "Staff"
    user_department = (user_department or "general").lower()
    
    # Get policy for this role
    policy = ROLE_POLICIES.get(user_role)
    
    # If role not found, default to own department + general
    if not policy:
        allowed = [user_department, "general"]
        # Remove duplicates and filter to valid departments
        return list(set(dept for dept in allowed if dept in ALL_DEPARTMENTS))
    
    # Check for all_departments privilege
    if policy.get("all_departments", False):
        return ALL_DEPARTMENTS.copy()
    
    # Check for fixed_departments (ignores user's home department)
    if "fixed_departments" in policy:
        fixed = policy["fixed_departments"]
        # Ensure all are valid
        return [dept for dept in fixed if dept in ALL_DEPARTMENTS]
    
    # Build from inherit_own_department + extra_departments
    allowed = []
    
    if policy.get("inherit_own_department", False):
        # Add user's home department if valid
        if user_department in ALL_DEPARTMENTS:
            allowed.append(user_department)
    
    # Add any extra departments
    if "extra_departments" in policy:
        allowed.extend(policy["extra_departments"])
    
    # Remove duplicates and ensure all are valid
    allowed = list(set(dept for dept in allowed if dept in ALL_DEPARTMENTS))
    
    # If somehow we end up with nothing, at least give them general
    if not allowed:
        allowed = ["general"]
    
    return allowed


def check_access(user_role: str, user_department: str, target_department: str) -> bool:
    """
    Check if a user has access to a specific department.
    
    Args:
        user_role: User's role
        user_department: User's home department
        target_department: Department to check access for
        
    Returns:
        True if user can access the target department, False otherwise
    """
    allowed = get_allowed_departments(user_role, user_department)
    return target_department.lower() in allowed


def get_role_description(user_role: str) -> str:
    """
    Get a human-readable description of what a role can access.
    
    Args:
        user_role: User's role
        
    Returns:
        Description string
    """
    policy = ROLE_POLICIES.get(user_role)
    
    if not policy:
        return "Access to own department and general documents"
    
    if policy.get("all_departments", False):
        return "Full access to all departments"
    
    if "fixed_departments" in policy:
        depts = ", ".join(policy["fixed_departments"])
        return f"Access to: {depts}"
    
    if policy.get("inherit_own_department", False):
        extra = policy.get("extra_departments", [])
        if extra:
            extra_str = ", ".join(extra)
            return f"Access to own department and: {extra_str}"
        return "Access to own department only"
    
    return "Limited access"


# Example usage and testing
if __name__ == "__main__":
    print("RBAC Policy Examples:\n")
    
    test_cases = [
        ("Intern", "it"),
        ("Staff", "hr"),
        ("HR_Officer", "hr"),
        ("Manager", "finance"),
        ("SecurityAnalyst", "security"),
        ("SysAdmin", "it"),
        ("Auditor", "compliance"),
        ("Executive", "executive"),
    ]
    
    for role, dept in test_cases:
        allowed = get_allowed_departments(role, dept)
        desc = get_role_description(role)
        print(f"{role} ({dept}):")
        print(f"  Allowed: {allowed}")
        print(f"  Description: {desc}")
        print()
