"""
Service para lógica de negócio de Lead.
"""
from typing import List, Optional
from app.schemas.lead_schema import LeadCreate, LeadResponse
from app.repositories.lead_repository import LeadRepository
from app.services.external_api_service import ExternalAPIService
from app.models.lead import Lead


class LeadService:
    """Service com a lógica de negócio para Lead."""
    
    def __init__(self):
        self.repository = LeadRepository()
        self.external_api = ExternalAPIService()
    
    async def create_lead(self, lead_data: LeadCreate) -> LeadResponse:
        """
        Cria um novo lead.
        
        Fluxo:
        1. Recebe dados do lead
        2. Busca birth_date da API externa
        3. Salva no MongoDB
        4. Retorna lead criado
        
        Args:
            lead_data: Dados do lead a ser criado
            
        Returns:
            LeadResponse com o lead criado (incluindo ID e birth_date)
        """
        # 1. Buscar birth_date da API externa
        birth_date = await self.external_api.get_birth_date()
        
        # 2. Preparar dados para salvar
        lead_dict = {
            "name": lead_data.name,
            "email": lead_data.email,
            "phone": lead_data.phone,
            "birth_date": birth_date  # Pode ser None se API falhar
        }
        
        # 3. Salvar no MongoDB
        created_lead = await self.repository.create(lead_dict)
        
        # 4. Converter para LeadResponse
        return LeadResponse(
            id=created_lead.id,
            name=created_lead.name,
            email=created_lead.email,
            phone=created_lead.phone,
            birth_date=created_lead.birth_date
        )
    
    async def get_all_leads(self) -> List[LeadResponse]:
        """
        Retorna todos os leads cadastrados.
        
        Returns:
            Lista de LeadResponse
        """
        leads = await self.repository.get_all()
        
        return [
            LeadResponse(
                id=lead.id,
                name=lead.name,
                email=lead.email,
                phone=lead.phone,
                birth_date=lead.birth_date
            )
            for lead in leads
        ]
    
    async def get_lead_by_id(self, lead_id: str) -> Optional[LeadResponse]:
        """
        Busca um lead específico por ID.
        
        Args:
            lead_id: ID do lead
            
        Returns:
            LeadResponse ou None se não encontrado
        """
        lead = await self.repository.get_by_id(lead_id)
        
        if not lead:
            return None
        
        return LeadResponse(
            id=lead.id,
            name=lead.name,
            email=lead.email,
            phone=lead.phone,
            birth_date=lead.birth_date
        ) 