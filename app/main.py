"""
Aplicação principal FastAPI - Lead Management API.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config.settings import settings
from app.core.database import db
from app.api.routes import lead_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gerencia o ciclo de vida da aplicação.
    Conecta ao MongoDB no startup e desconecta no shutdown.
    """
    # Startup
    print("🚀 Iniciando aplicação...")
    await db.connect_db()
    print("✅ Aplicação pronta!")
    
    yield
    
    # Shutdown
    print("🔴 Encerrando aplicação...")
    await db.close_db()
    print("✅ Aplicação encerrada!")


# Criar aplicação FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS (permite requisições de qualquer origem)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(lead_routes.router)


@app.get("/", tags=["health"])
async def root():
    """
    Endpoint raiz - Health check.
    """
    return {
        "message": "Lead Management API",
        "version": settings.APP_VERSION,
        "status": "running"
    }


@app.get("/health", tags=["health"])
async def health_check():
    """
    Verifica se a API está funcionando.
    """
    return {
        "status": "healthy",
        "database": "connected"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    ) 