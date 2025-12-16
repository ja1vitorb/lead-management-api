"""
Repository para operações de Lead no MongoDB.
"""
from typing import List, Optional
from bson import ObjectId
from app.core.database import db
from app.models.lead import Lead


class LeadRepository:
    """Repository para acesso aos dados de Lead."""
    
    def __init__(self):
        self.collection_name = "leads"
    
    @property
    def collection(self):
        """Retorna a collection do MongoDB."""
        return db.get_database()[self.collection_name]
    
    async def create(self, lead_data: dict) -> Lead:
        """
        Cria um novo lead no MongoDB.
        
        Args:
            lead_data: Dicionário com os dados do lead
            
        Returns:
            Lead criado com ID
        """
        result = await self.collection.insert_one(lead_data)
        
        # Buscar o lead criado para retornar completo
        created_lead = await self.collection.find_one({"_id": result.inserted_id})
        return Lead.from_dict(created_lead)
    
    async def get_all(self) -> List[Lead]:
        """
        Retorna todos os leads.
        
        Returns:
            Lista de todos os leads
        """
        leads = []
        cursor = self.collection.find()
        
        async for document in cursor:
            leads.append(Lead.from_dict(document))
        
        return leads
    
    async def get_by_id(self, lead_id: str) -> Optional[Lead]:
        """
        Busca um lead por ID.
        
        Args:
            lead_id: ID do lead (string)
            
        Returns:
            Lead encontrado ou None
        """
        try:
            # Converter string para ObjectId
            object_id = ObjectId(lead_id)
            document = await self.collection.find_one({"_id": object_id})
            
            if document:
                return Lead.from_dict(document)
            return None
            
        except Exception as e:
            print(f"❌ Erro ao buscar lead por ID: {e}")
            return None
    
    async def delete_all(self):
        """
        Deleta todos os leads (útil para testes).
        """
        result = await self.collection.delete_many({})
        return result.deleted_count 