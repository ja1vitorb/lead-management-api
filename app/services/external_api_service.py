"""
Serviço para integração com API externa (DummyJSON).
"""
import httpx
from typing import Optional
from app.config.settings import settings


class ExternalAPIService:
    """Serviço para buscar dados de APIs externas."""
    
    def __init__(self):
        self.api_url = settings.EXTERNAL_API_URL
        self.timeout = 10.0  # segundos
    
    async def get_birth_date(self) -> Optional[str]:
        """
        Busca a data de nascimento da API externa.
        
        Returns:
            str: Data de nascimento no formato 'YYYY-MM-DD' ou None em caso de falha
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(self.api_url)
                response.raise_for_status()
                
                data = response.json()
                birth_date = data.get("birthDate")
                
                if birth_date:
                    print(f"✅ Birth date obtido da API externa: {birth_date}")
                    return birth_date
                else:
                    print("⚠️ Campo 'birthDate' não encontrado na resposta da API")
                    return None
                    
        except httpx.TimeoutException:
            print(f"❌ Timeout ao acessar API externa após {self.timeout}s")
            return None
            
        except httpx.HTTPStatusError as e:
            print(f"❌ Erro HTTP ao acessar API externa: {e.response.status_code}")
            return None
            
        except httpx.RequestError as e:
            print(f"❌ Erro de conexão com API externa: {str(e)}")
            return None
            
        except Exception as e:
            print(f"❌ Erro inesperado ao acessar API externa: {str(e)}")
            return None 