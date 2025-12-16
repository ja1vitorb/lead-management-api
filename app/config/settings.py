"""
Configurações da aplicação carregadas de variáveis de ambiente.
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configurações da aplicação."""
    
    # MongoDB
    MONGODB_URL: str
    MONGODB_DB_NAME: str
    
    # API Externa
    EXTERNAL_API_URL: str
    
    # Aplicação
    APP_NAME: str = "Lead Management API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "API para gerenciamento de leads"
    DEBUG: bool = True
    
    # Servidor
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    class Config:
        """Configuração do Pydantic."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Instância única de configurações
settings = Settings()