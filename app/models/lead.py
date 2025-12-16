"""
Modelo de domínio do Lead.
"""
from typing import Optional
from datetime import datetime


class Lead:
    """Entidade Lead do domínio."""
    
    def __init__(
        self,
        name: str,
        email: str,
        phone: str,
        birth_date: Optional[str] = None,
        id: Optional[str] = None,
        created_at: Optional[datetime] = None
    ):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.birth_date = birth_date
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self) -> dict:
        """Converte o Lead para dicionário (para MongoDB)."""
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "birth_date": self.birth_date,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Lead":
        """Cria um Lead a partir de um dicionário (do MongoDB)."""
        return cls(
            id=str(data.get("_id", "")),
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            birth_date=data.get("birth_date"),
            created_at=data.get("created_at")
        )
    
    def __repr__(self):
        return f"Lead(id={self.id}, name={self.name}, email={self.email})"