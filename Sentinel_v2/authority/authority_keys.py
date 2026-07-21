import os
import json
import nacl.signing
from typing import Optional

class AuthorityKeys:
    """Manages authority keypair storage"""
    
    def __init__(self, storage_dir: str = "storage/authority"):
        self.storage_dir = storage_dir
        self._ensure_storage_dir()
    
    def _ensure_storage_dir(self):
        os.makedirs(self.storage_dir, exist_ok=True)
    
    def generate_and_save(self) -> Tuple[nacl.signing.SigningKey, nacl.signing.VerifyKey]:
        """Generate new authority keys and save them"""
        signing_key = nacl.signing.SigningKey.generate()
        verify_key = signing_key.verify_key
        
        # Save private key (SECURE - in production use proper key management)
        private_path = os.path.join(self.storage_dir, "authority_private.key")
        with open(private_path, 'w') as f:
            f.write(signing_key.encode(encoder=nacl.encoding.Base64Encoder).decode('utf-8'))
        
        # Save public key
        public_path = os.path.join(self.storage_dir, "authority_public.key")
        with open(public_path, 'w') as f:
            f.write(verify_key.encode(encoder=nacl.encoding.Base64Encoder).decode('utf-8'))
        
        return signing_key, verify_key
    
    def load_signing_key(self) -> Optional[nacl.signing.SigningKey]:
        """Load authority signing key"""
        path = os.path.join(self.storage_dir, "authority_private.key")
        if not os.path.exists(path):
            return None
        with open(path, 'r') as f:
            key_data = f.read().strip()
        return nacl.signing.SigningKey(key_data, encoder=nacl.encoding.Base64Encoder)
    
    def load_verify_key(self) -> Optional[nacl.signing.VerifyKey]:
        """Load authority verification key"""
        path = os.path.join(self.storage_dir, "authority_public.key")
        if not os.path.exists(path):
            return None
        with open(path, 'r') as f:
            key_data = f.read().strip()
        return nacl.signing.VerifyKey(key_data, encoder=nacl.encoding.Base64Encoder)