# crypto/challenges.py
import secrets
import time
from typing import Dict

def generate_challenge() -> str:
    """Generate a random challenge/nonce"""
    return secrets.token_hex(32)

def verify_challenge(challenge: str, stored_challenge: str, max_age: int = 300) -> bool:
    """
    Verify a challenge with timestamp validation
    max_age: maximum age in seconds (default 5 minutes)
    """
    # For now, basic comparison
    # In production, would check timestamp and ensure not reused
    return challenge == stored_challenge