# API de Gerenciamento de Tarefas 📋

Uma API REST construída com FastAPI para gerenciar tarefas com autenticação e banco de dados SQLite.

## Estrutura do Projeto

```
task_api/
├── app/
│   ├── __init__.py          # Inicializador do pacote
│   ├── main.py              # Aplicação FastAPI principal
│   ├── routes.py            # Rotas da API
│   ├── models.py            # Modelos de banco de dados
│   ├── schemas.py           # Schemas Pydantic
│   ├── database.py          # Configuração do banco de dados
│   └── auth.py              # Autenticação e segurança
├── requirements.txt         # Dependências do projeto
├── .gitignore              # Arquivo para excluir arquivos do Git
└── tasks.db               # Banco de dados SQLite (local)
```

## Instalação

### 1. Clonar o repositório

**Com SSH (mais rápido):**
```bash
git clone git@github.com:itzbrunin/API-de-Gerenciamento-de-Tarefas.git
cd API-de-Gerenciamento-de-Tarefas
```

**Com HTTPS (se SSH não funcionar):**
```bash
git clone https://github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas.git
cd API-de-Gerenciamento-de-Tarefas
```

### 2. Criar ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

## Executar a API

```bash
uvicorn app.main:app --reload
```

A API estará disponível em: **http://localhost:8000**

## Documentação Interativa

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints Principais

### Autenticação
- `POST /auth/login` - Fazer login
- `POST /auth/register` - Registrar novo usuário

### Tarefas
- `GET /tasks` - Listar todas as tarefas
- `POST /tasks` - Criar nova tarefa
- `GET /tasks/{id}` - Obter tarefa específica
- `PUT /tasks/{id}` - Atualizar tarefa
- `DELETE /tasks/{id}` - Deletar tarefa

## Dependências

Veja `requirements.txt` para lista completa das dependências.

Principais:
- **FastAPI** - Framework web moderno
- **SQLAlchemy** - ORM para banco de dados
- **Pydantic** - Validação de dados
- **python-jose** - Autenticação JWT
- **passlib** - Hash de senhas
- **SQLite** - Banco de dados

## Desenvolvimento

### Adicionar mudanças ao Git
```bash
git add .
git commit -m "Descrição das mudanças"
git push origin main
```

## Autor

**itzbrunin** - GitHub

## Licença

Este projeto está disponível sob a licença MIT.

---

### Status do Repositório

✅ Projeto enviado para: https://github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas
