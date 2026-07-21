import os
import json
from typing import Optional
from models import Credential, Proof
from crypto import encode_public_key
from wallet.wallet_keys import WalletKeys
from wallet.proof_engine import ProofEngine

class Wallet:
    """User wallet for storing credentials and generating proofs"""
    
    def __init__(self, storage_dir: str = "storage/wallet"):
        self.storage_dir = storage_dir
        self.keys = WalletKeys(storage_dir)
        self.signing_key = self.keys.load_signing_key()
        self.verify_key = self.keys.load_verify_key()
        
        if not self.signing_key or not self.verify_key:
            self.signing_key, self.verify_key = self.keys.generate_and_save()
        
        self.proof_engine = ProofEngine(self.signing_key, self.verify_key)
        self._ensure_storage_dir()
    
    def _ensure_storage_dir(self):
        os.makedirs(self.storage_dir, exist_ok=True)
    
    def store_credential(self, credential: Credential):
        """Store a credential in the wallet"""
        path = os.path.join(self.storage_dir, "credential.json")
        with open(path, 'w') as f:
            json.dump(credential.to_dict(), f, indent=2)
    
    def load_credential(self) -> Optional[Credential]:
        """Load stored credential"""
        path = os.path.join(self.storage_dir, "credential.json")
        if not os.path.exists(path):
            return None
        with open(path, 'r') as f:
            data = json.load(f)
        return Credential.from_dict(data)
    
    def generate_proof(self, claim_type: str, challenge: str) -> Optional[Proof]:
        """Generate a proof for a claim"""
        credential = self.load_credential()
        if not credential:
            return None
        
        if claim_type == "AGE_OVER_18":
            return self.proof_engine.generate_age_proof(credential.birth_year, challenge)
        
        return None
    
    def get_public_key(self) -> str:
        """Get wallet public key"""
        return encode_public_key(self.verify_key)