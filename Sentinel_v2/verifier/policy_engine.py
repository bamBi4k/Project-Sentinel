from typing import Dict, Any

class PolicyEngine:
    """Enforces verification policies"""
    
    def __init__(self):
        self.policies = {}
    
    def add_policy(self, claim_type: str, required_value: Any):
        """Add a verification policy"""
        self.policies[claim_type] = required_value
    
    def check_policy(self, claim_type: str, value: Any) -> bool:
        """Check if a claim meets policy requirements"""
        if claim_type not in self.policies:
            return False
        
        if claim_type == "AGE_OVER_18":
            return value is True
        
        return value == self.policies[claim_type]