import json
from typing import Dict, Any, Optional
from crypto import (
    verify_signature, decode_public_key,
    hash_data
)
from models import Proof

class Verifier:
    """Verifies proofs and credentials"""
    
    def __init__(self):
        self.authority_public_key = None
    
    def set_authority_public_key(self, public_key: str):
        """Set the authority's public key for verification"""
        self.authority_public_key = decode_public_key(public_key)
    
    def verify_proof(self, proof_data: Dict[str, Any]) -> bool:
        """Verify a proof signature"""
        try:
            proof = Proof.from_dict(proof_data)
            
            # Recreate the signed data
            proof_dict = proof.to_dict()
            proof_dict.pop('signature', None)
            proof_json = json.dumps(proof_dict, sort_keys=True)
            
            # Verify signature
            signature = bytes.fromhex(proof.signature)
            verify_key = decode_public_key(proof.public_key)
            
            return verify_signature(verify_key, proof_json.encode('utf-8'), signature)
        except Exception as e:
            print(f"Verification error: {e}")
            return False
    
    def verify_credential(self, credential_data: Dict[str, Any]) -> bool:
        """Verify a credential signature (issued by authority)"""
        try:
            from models import Credential
            credential = Credential.from_dict(credential_data)
            
            # Verify authority signature
            if not self.authority_public_key:
                print("Authority public key not set!")
                return False
            
            # Recreate the signed data
            cred_dict = credential.to_dict()
            cred_dict.pop('signature', None)
            cred_json = json.dumps(cred_dict, sort_keys=True)
            cred_hash = hash_data(cred_json.encode('utf-8'))
            
            signature = bytes.fromhex(credential.signature)
            
            return verify_signature(
                self.authority_public_key,
                cred_hash.encode('utf-8'),
                signature
            )
        except Exception as e:
            print(f"Credential verification error: {e}")
            return False