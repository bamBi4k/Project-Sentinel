import json
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, Any

@dataclass
class Credential:
    """Represents a signed credential issued by the authority"""
    user_id: str
    birth_year: int
    age_over_18: bool
    issuer: str
    issued_at: str
    signature: str = ""
    public_key: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict())
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Credential':
        return cls(**data)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'Credential':
        return cls.from_dict(json.loads(json_str))