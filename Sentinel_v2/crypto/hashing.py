# crypto/hashing.py
import hashlib
import json
from typing import Union

def hash_data(data: Union[str, bytes]) -> str:
    """SHA-256 hash of data"""
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()

def hash_credential(credential_data: dict) -> str:
    """Hash a credential dictionary"""
    json_str = json.dumps(credential_data, sort_keys=True)
    return hash_data(json_str)