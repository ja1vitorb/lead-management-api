"""
Gerenciamento da conexão com MongoDB.
"""
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.config.settings import settings


class Database:
    """Gerenciador de conexão com MongoDB."""
    
    client: AsyncIOMotorClient = None
    database: AsyncIOMotorDatabase = None
    
    @classmethod
    async def connect_db(cls):
        """Conecta ao MongoDB."""
        try:
            cls.client = AsyncIOMotorClient(settings.MONGODB_URL)
            cls.database = cls.client[settings.MONGODB_DB_NAME]
            
            # Testar conexão
            await cls.client.admin.command('ping')
            print(f"✅ Conectado ao MongoDB: {settings.MONGODB_DB_NAME}")
            
        except Exception as e:
            print(f"❌ Erro ao conectar ao MongoDB: {e}")
            raise
    
    @classmethod
    async def close_db(cls):
        """Fecha a conexão com MongoDB."""
        if cls.client:
            cls.client.close()
            print("✅ Conexão com MongoDB fechada")
    
    @classmethod
    def get_database(cls) -> AsyncIOMotorDatabase:
        """Retorna a instância do database."""
        if cls.database is None:
            raise Exception("Database não está conectado. Execute connect_db() primeiro.")
        return cls.database


# Instância global
db = Database() 