# Lead Management API

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-009688.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-7.0-green.svg)
![Docker](https://img.shields.io/badge/Docker-compose-2496ED.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Sobre o Projeto

API RESTful para gerenciamento de leads desenvolvida com FastAPI, MongoDB e integração com serviços externos. O sistema permite o cadastro, consulta e listagem de leads, enriquecendo automaticamente os dados através de integração com APIs externas.

### Objetivo

Fornecer uma solução robusta e escalável para gestão de leads, automatizando a coleta de informações complementares (data de nascimento) via API externa e garantindo persistência confiável dos dados.

## Funcionalidades

- Cadastro de Leads: Criação de novos leads com validação automática de dados
- Enriquecimento Automático: Busca automática de data de nascimento via API externa (DummyJSON)
- Consulta Individual: Recuperação de detalhes de um lead específico por ID
- Listagem Completa: Visualização de todos os leads cadastrados
- Tratamento de Erros: Gestão adequada de falhas na integração externa
- Documentação Interativa: Swagger UI e ReDoc automáticos

## Tecnologias Utilizadas

- **Python 3.11+** - Linguagem de programação
- **FastAPI** - Framework web moderno e de alta performance
- **MongoDB** - Banco de dados NoSQL
- **Motor** - Driver assíncrono para MongoDB
- **Pydantic** - Validação de dados e serialização
- **HTTPX** - Cliente HTTP assíncrono
- **Docker & Docker Compose** - Containerização e orquestração

## Arquitetura

O projeto segue princípios de Clean Architecture com separação clara de responsabilidades:

```
app/
├── api/                    # API Layer (Endpoints REST)
│   └── routes/
│       └── lead_routes.py
├── services/               # Service Layer (Lógica de Negócio)
│   ├── lead_service.py
│   └── external_api_service.py
├── repositories/           # Repository Layer (Acesso a Dados)
│   └── lead_repository.py
├── models/                 # Domain Models
│   └── lead.py
├── schemas/                # Pydantic Schemas (Validação)
│   └── lead_schema.py
├── core/                   # Core Functionality
│   └── database.py
├── config/                 # Configurações
│   └── settings.py
└── main.py                 # Entry Point
```

### Camadas da Aplicação

**API Layer**: Endpoints REST, validação de entrada e formatação de resposta

**Service Layer**: Orquestração de operações, regras de negócio e coordenação entre camadas

**Repository Layer**: Operações CRUD e abstração do acesso ao MongoDB

**External Services**: Integração com APIs de terceiros (DummyJSON)

### Fluxo de Criação de Lead

1. Cliente envia requisição POST com dados do lead
2. API Layer valida os dados através dos schemas Pydantic
3. Service Layer consulta API externa para obter data de nascimento
4. Em caso de sucesso, dados são enriquecidos com birth_date
5. Repository persiste o lead no MongoDB
6. Resposta é retornada ao cliente com status 201

## Instalação e Configuração

### Pré-requisitos

- Python 3.11 ou superior
- Docker e Docker Compose
- Git

### 1. Clonar o Repositório

```bash
git clone https://github.com/ja1vitorb/lead-management-api.git
cd lead-management-api
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```bash
cp .env.example .env
```

Edite o `.env` com suas configurações:

```env
MONGODB_URL="mongodb://admin:admin123@localhost:27017/leads_db?authSource=admin"
MONGODB_DB_NAME=leads_db
EXTERNAL_API_URL=https://dummyjson.com/users/1
APP_NAME=Lead Management API
APP_VERSION=1.0.0
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

### 3. Iniciar MongoDB com Docker Compose

```bash
docker-compose up -d
```

Verificar status:

```bash
docker-compose ps
```

### 4. Criar Ambiente Virtual Python

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 5. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a Aplicação

```bash
uvicorn app.main:app --reload
```

A API estará disponível em: `http://localhost:8000`

## Documentação da API

### Endpoints Disponíveis

| Método | Endpoint | Descrição | Status Code |
|--------|----------|-----------|-------------|
| POST | `/leads` | Cria um novo lead | 201 |
| GET | `/leads` | Lista todos os leads | 200 |
| GET | `/leads/{id}` | Busca lead por ID | 200, 404 |
| GET | `/` | Health check | 200 |
| GET | `/health` | Status da aplicação | 200 |

### Documentação Interativa

Após iniciar a aplicação, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### Exemplos de Requisições

#### Criar Lead

**Endpoint:** `POST /leads`

**Request Body:**
```json
{
  "name": "João Silva",
  "email": "joao.silva@example.com",
  "phone": "+55 11 98765-4321"
}
```

**Response (201 Created):**
```json
{
  "id": "6941c64f83c2a6e07e1558af",
  "name": "João Silva",
  "email": "joao.silva@example.com",
  "phone": "+55 11 98765-4321",
  "birth_date": "1996-5-30"
}
```

**Comando cURL:**
```bash
curl -X POST "http://localhost:8000/leads" \
  -H "Content-Type: application/json" \
  -d '{"name":"João Silva","email":"joao.silva@example.com","phone":"+55 11 98765-4321"}'
```

#### Listar Todos os Leads

**Endpoint:** `GET /leads`

**Response (200 OK):**
```json
[
  {
    "id": "6941c64f83c2a6e07e1558af",
    "name": "João Silva",
    "email": "joao.silva@example.com",
    "phone": "+55 11 98765-4321",
    "birth_date": "1996-5-30"
  }
]
```

**Comando cURL:**
```bash
curl -X GET "http://localhost:8000/leads"
```

#### Buscar Lead por ID

**Endpoint:** `GET /leads/{lead_id}`

**Response (200 OK):**
```json
{
  "id": "6941c64f83c2a6e07e1558af",
  "name": "João Silva",
  "email": "joao.silva@example.com",
  "phone": "+55 11 98765-4321",
  "birth_date": "1996-5-30"
}
```

**Response (404 Not Found):**
```json
{
  "detail": "Lead com ID 507f1f77bcf86cd799439011 não encontrado"
}
```

**Comando cURL:**
```bash
curl -X GET "http://localhost:8000/leads/6941c64f83c2a6e07e1558af"
```

## Integração com API Externa

### Funcionamento

Durante a criação de um lead, o sistema realiza uma requisição assíncrona para a API externa DummyJSON:

- **URL**: https://dummyjson.com/users/1
- **Método**: GET
- **Timeout**: 10 segundos
- **Campo extraído**: `birthDate`

### Tratamento de Falhas

A aplicação implementa um tratamento robusto de falhas na integração externa:

**Cenários tratados:**
- Timeout de requisição
- Erro HTTP (4xx, 5xx)
- Erro de conexão
- Campo `birthDate` ausente na resposta
- Erro inesperado

**Comportamento em caso de falha:**
1. O lead é criado normalmente no banco de dados
2. O campo `birth_date` é definido como `null`
3. Um log de erro é registrado no console
4. A operação principal não é interrompida
5. Status code 201 é retornado ao cliente

**Exemplo de resposta com falha na API externa:**
```json
{
  "id": "6941c64f83c2a6e07e1558af",
  "name": "João Silva",
  "email": "joao.silva@example.com",
  "phone": "+55 11 98765-4321",
  "birth_date": null
}
```

## Docker

### Configuração do MongoDB

O projeto utiliza Docker Compose para orquestrar o MongoDB. A configuração inclui:

- MongoDB 7.0
- Autenticação habilitada
- Volume persistente
- Healthcheck configurado
- Rede isolada

### Executar com Docker Compose

```bash
# Iniciar serviços
docker-compose up -d

# Verificar status
docker-compose ps

# Ver logs
docker-compose logs -f mongodb

# Parar serviços
docker-compose down

# Parar e remover volumes (apaga dados)
docker-compose down -v
```

### Dockerfile da Aplicação

O projeto inclui um Dockerfile para containerizar a aplicação FastAPI:

```bash
# Build da imagem
docker build -t lead-management-api .

# Executar container
docker run -p 8000:8000 --env-file .env lead-management-api
```

## Testes

### Testes Manuais via Swagger UI

1. Acesse http://localhost:8000/docs
2. Selecione o endpoint desejado
3. Clique em "Try it out"
4. Preencha os parâmetros
5. Clique em "Execute"
6. Analise a resposta

### Testes via cURL

```bash
# Health check
curl http://localhost:8000/health

# Criar lead
curl -X POST "http://localhost:8000/leads" \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","phone":"123456789"}'

# Listar leads
curl http://localhost:8000/leads

# Buscar por ID
curl http://localhost:8000/leads/{lead_id}
```

### Verificação no MongoDB

**Via Mongo Express (interface web):**
```
http://localhost:8081
```

**Via MongoDB CLI:**
```bash
docker exec -it lead-mongodb mongosh -u admin -p admin123 --authenticationDatabase admin
```

**Comandos úteis no mongosh:**
```javascript
use leads_db
db.leads.find().pretty()
db.leads.countDocuments()
```

## Troubleshooting

### MongoDB não conecta

**Sintoma:** `Exception: Database não está conectado`

**Diagnóstico:**
```bash
docker-compose ps
docker-compose logs mongodb
```

**Solução:**
```bash
docker-compose restart mongodb
```

### Porta 8000 já em uso

**Sintoma:** `Error: [Errno 48] Address already in use`

**Solução 1 - Alterar porta:**
```env
# Edite .env
PORT=8001
```

**Solução 2 - Finalizar processo:**

Windows:
```bash
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

Linux/Mac:
```bash
lsof -ti:8000 | xargs kill -9
```

### Erro de importação

**Sintoma:** `ModuleNotFoundError: No module named 'app'`

**Solução:**
```bash
# Ativar ambiente virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Reinstalar dependências
pip install -r requirements.txt
```

### API externa timeout

**Sintoma:** Leads criados com `birth_date: null`

**Causa:** API externa DummyJSON indisponível ou lenta

**Verificação:**
```bash
curl https://dummyjson.com/users/1
```

**Comportamento esperado:** Este é o comportamento correto. O sistema continua operando normalmente mesmo quando a API externa falha.

## Estrutura do Banco de Dados

### Collection: leads

**Schema:**
```javascript
{
  "_id": ObjectId("6941c64f83c2a6e07e1558af"),
  "name": String,
  "email": String,
  "phone": String,
  "birth_date": String | null,
  "created_at": ISODate("2025-12-16T20:51:23.000Z")
}
```

**Índices:**
- `_id`: Índice único criado automaticamente pelo MongoDB

## Decisões Técnicas

### Por que FastAPI?

- Performance superior através de async/await
- Validação automática com Pydantic
- Documentação automática (Swagger/ReDoc)
- Type hints nativos do Python
- Amplamente adotado pela indústria

### Por que MongoDB?

- Flexibilidade de schema para evolução do modelo
- Excelente performance em operações de leitura/escrita
- Escalabilidade horizontal
- Adequado para dados semi-estruturados

### Por que Motor?

- Driver oficial assíncrono para MongoDB
- Totalmente compatível com async/await do FastAPI
- Melhor performance em operações I/O bound

### Arquitetura em Camadas

A separação em camadas proporciona:
- Baixo acoplamento entre componentes
- Facilidade de manutenção e testes
- Possibilidade de trocar implementações
- Código mais limpo e organizado

## Contribuindo

Contribuições são bem-vindas. Para contribuir:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feat/nova-feature`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona nova feature'`)
4. Push para a branch (`git push origin feat/nova-feature`)
5. Abra um Pull Request

### Padrão de Commits

O projeto utiliza Conventional Commits:

- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Mudanças na documentação
- `refactor:` - Refatoração de código
- `test:` - Adição ou modificação de testes
- `chore:` - Mudanças em ferramentas, configurações, etc

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

**João Vitor Barbosa Dantas**

- GitHub: [@ja1vitorb](https://github.com/ja1vitorb)
- LinkedIn: [João Vitor Barbosa Dantas](https://www.linkedin.com/in/ja1vitorb)
- Email: joao.dantas@blips.com.br

## Referências

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Motor Documentation](https://motor.readthedocs.io/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Docker Documentation](https://docs.docker.com/)

---

Desenvolvido como parte de desafio técnico para demonstração de habilidades em desenvolvimento de APIs REST, arquitetura de software e boas práticas de programação.