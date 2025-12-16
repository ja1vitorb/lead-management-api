"""
Schemas Pydantic para validação de dados de Lead.
"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date


class LeadCreate(BaseModel):
    """Schema para criação de Lead (dados de entrada)."""
    
    name: str = Field(..., min_length=1, max_length=100, description="Nome do lead")
    email: EmailStr = Field(..., description="Email válido do lead")
    phone: str = Field(..., min_length=8, max_length=20, description="Telefone do lead")
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "João Silva",
                "email": "joao.silva@example.com",
                "phone": "+55 11 98765-4321"
            }
        }


class LeadResponse(BaseModel):
    """Schema para resposta de Lead (dados de saída)."""
    
    id: str = Field(..., description="ID único do lead")
    name: str = Field(..., description="Nome do lead")
    email: str = Field(..., description="Email do lead")
    phone: str = Field(..., description="Telefone do lead")
    birth_date: Optional[str] = Field(None, description="Data de nascimento (formato: YYYY-MM-DD)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "name": "João Silva",
                "email": "joao.silva@example.com",
                "phone": "+55 11 98765-4321",
                "birth_date": "1990-05-15"
            }
        }  