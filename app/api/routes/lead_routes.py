"""
Rotas da API para gerenciamento de Leads.
"""
from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.lead_schema import LeadCreate, LeadResponse
from app.services.lead_service import LeadService

# Criar router
router = APIRouter(
    prefix="/leads",
    tags=["leads"]
)

# Instanciar service
lead_service = LeadService()


@router.post(
    "",
    response_model=LeadResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar novo lead",
    description="Cria um novo lead e busca automaticamente a data de nascimento de uma API externa."
)
async def create_lead(lead_data: LeadCreate):
    """
    Cria um novo lead.
    
    - **name**: Nome completo do lead
    - **email**: Email válido do lead
    - **phone**: Telefone do lead
    
    A data de nascimento (birth_date) é obtida automaticamente de uma API externa.
    Se a API externa falhar, o lead é criado com birth_date = null.
    """
    try:
        lead = await lead_service.create_lead(lead_data)
        return lead
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar lead: {str(e)}"
        )


@router.get(
    "",
    response_model=List[LeadResponse],
    summary="Listar todos os leads",
    description="Retorna uma lista com todos os leads cadastrados."
)
async def get_all_leads():
    """
    Lista todos os leads cadastrados.
    
    Retorna uma lista vazia se não houver leads.
    """
    try:
        leads = await lead_service.get_all_leads()
        return leads
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar leads: {str(e)}"
        )


@router.get(
    "/{lead_id}",
    response_model=LeadResponse,
    summary="Buscar lead por ID",
    description="Retorna os detalhes de um lead específico pelo seu ID."
)
async def get_lead_by_id(lead_id: str):
    """
    Busca um lead específico por ID.
    
    - **lead_id**: ID do lead no formato MongoDB ObjectId
    
    Retorna 404 se o lead não for encontrado.
    """
    try:
        lead = await lead_service.get_lead_by_id(lead_id)
        
        if not lead:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Lead com ID {lead_id} não encontrado"
            )
        
        return lead
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar lead: {str(e)}"
        ) 