# crypto/signatures.py
import nacl.signing
import nacl.encoding
import base64
from typing import Tuple

def generate_keypair() -> Tuple[nacl.signing.SigningKey, nacl.signing.VerifyKey]:
    """Generate Ed25519 keypair"""
    signing_key = nacl.signing.SigningKey.generate()
    verify_key = signing_key.verify_key
    return signing_key, verify_key

def sign_data(signing_key: nacl.signing.SigningKey, data: bytes) -> bytes:
    """Sign data using Ed25519"""
    signed = signing_key.sign(data)
    return signed.signature

def verify_signature(verify_key: nacl.signing.VerifyKey, data: bytes, signature: bytes) -> bool:
    """Verify Ed25519 signature"""
    try:
        verify_key.verify(data, signature)
        return True
    except nacl.exceptions.BadSignatureError:
        return False

def encode_public_key(verify_key: nacl.signing.VerifyKey) -> str:
    """Encode public key to base64 string"""
    return base64.b64encode(bytes(verify_key)).decode('utf-8')

def decode_public_key(encoded_key: str) -> nacl.signing.VerifyKey:
    """Decode public key from base64 string"""
    key_bytes = base64.b64decode(encoded_key)
    return nacl.signing.VerifyKey(key_bytes)