import json
from datetime import datetime
from typing import Optional
from crypto import (
    generate_keypair, sign_data, encode_public_key,
    decode_public_key, hash_credential
)
from models import Credential
from authority.authority_keys import AuthorityKeys

class Issuer:
    """Issues signed credentials"""
    
    def __init__(self, storage_dir: str = "storage/authority"):
        self.keys = AuthorityKeys(storage_dir)
        self.signing_key = self.keys.load_signing_key()
        self.verify_key = self.keys.load_verify_key()
        
        if not self.signing_key or not self.verify_key:
            # Generate keys if they don't exist
            self.signing_key, self.verify_key = self.keys.generate_and_save()
    
    def issue_credential(self, user_id: str, birth_year: int) -> Credential:
        """Issue a signed credential for a user"""
        # Create credential
        credential = Credential(
            user_id=user_id,
            birth_year=birth_year,
            age_over_18=(2026 - birth_year) >= 18,
            issuer="SentinelAuthority",
            issued_at=datetime.now().isoformat(),
            public_key=encode_public_key(self.verify_key)
        )
        
        # Sign the credential
        credential_dict = credential.to_dict()
        # Remove signature field before hashing
        credential_dict.pop('signature', None)
        credential_hash = hash_credential(credential_dict)
        
        signature = sign_data(self.signing_key, credential_hash.encode('utf-8'))
        credential.signature = signature.hex()
        
        return credential
    
    def get_public_key(self) -> str:
        """Get authority public key"""
        return encode_public_key(self.verify_key)
    
    def get_signing_key(self):
        """Get authority signing key (internal use only)"""
        return self.signing_key