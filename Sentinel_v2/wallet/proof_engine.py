import json
from datetime import datetime
from typing import Dict, Any
from crypto import sign_data, encode_public_key
from models import Proof

class ProofEngine:
    """Generates cryptographic proofs from credentials"""
    
    def __init__(self, signing_key, verify_key):
        self.signing_key = signing_key
        self.verify_key = verify_key
    
    def generate_age_proof(self, birth_year: int, challenge: str) -> Proof:
        """Generate a proof that user is over 18"""
        is_over_18 = (datetime.now().year - birth_year) >= 18
        
        # Create proof
        proof = Proof(
            claim_type="AGE_OVER_18",
            value=is_over_18,
            challenge=challenge,
            timestamp=datetime.now().isoformat(),
            public_key=encode_public_key(self.verify_key)
        )
        
        # Sign the proof
        proof_dict = proof.to_dict()
        proof_dict.pop('signature', None)
        proof_json = json.dumps(proof_dict, sort_keys=True)
        
        signature = sign_data(self.signing_key, proof_json.encode('utf-8'))
        proof.signature = signature.hex()
        
        return proof