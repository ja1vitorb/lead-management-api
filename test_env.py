from dotenv import load_dotenv
from pathlib import Path
import os

# Encontrar o arquivo .env na raiz do projeto
env_path = Path(__file__).parent / '.env'
print(f"📁 Procurando .env em: {env_path}")
print(f"📄 Arquivo existe? {env_path.exists()}\n")

# Carregar o .env
loaded = load_dotenv(dotenv_path=env_path, override=True)
print(f"✅ .env carregado? {loaded}\n")

print("🔍 Testando variáveis de ambiente...\n")

# MongoDB
mongodb_url = os.getenv("MONGODB_URL")
mongodb_db = os.getenv("MONGODB_DB_NAME")
print(f"MONGODB_URL: {mongodb_url}")
print(f"MONGODB_DB_NAME: {mongodb_db}\n")

# API Externa
external_api = os.getenv("EXTERNAL_API_URL")
print(f"EXTERNAL_API_URL: {external_api}\n")

# App
app_name = os.getenv("APP_NAME")
app_version = os.getenv("APP_VERSION")
debug = os.getenv("DEBUG")
print(f"APP_NAME: {app_name}")
print(f"APP_VERSION: {app_version}")
print(f"DEBUG: {debug}\n")

# Server
host = os.getenv("HOST")
port = os.getenv("PORT")
print(f"HOST: {host}")
print(f"PORT: {port}\n")

# Verificar se todas estão definidas
required_vars = [
    "MONGODB_URL",
    "MONGODB_DB_NAME", 
    "EXTERNAL_API_URL",
    "APP_NAME"
]

missing = [var for var in required_vars if not os.getenv(var)]

if missing:
    print(f"❌ Variáveis faltando: {', '.join(missing)}")
else:
    print("🎉 Todas as variáveis obrigatórias estão definidas!")

# Debug: Mostrar TODAS as variáveis de ambiente
print("\n" + "="*50)
print("🔍 Debug - Variáveis que começam com APP_, MONGODB_, EXTERNAL_:")
for key, value in os.environ.items():
    if key.startswith(('APP_', 'MONGODB_', 'EXTERNAL_', 'HOST', 'PORT', 'DEBUG')):
        print(f"  {key} = {value}")