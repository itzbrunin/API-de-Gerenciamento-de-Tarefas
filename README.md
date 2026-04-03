# 🚀 Task API - Gerenciador de Tarefas com Autenticação

API RESTful desenvolvida com FastAPI para gerenciamento de tarefas com autenticação de usuários utilizando JWT.

---

## 📌 Sobre o projeto

Este projeto consiste em uma API completa que permite:

* Cadastro de usuários
* Autenticação com token JWT
* CRUD de tarefas
* Proteção de rotas
* Associação de tarefas a usuários

Cada usuário possui suas próprias tarefas, garantindo segurança e isolamento dos dados.

---

## 🛠️ Tecnologias utilizadas

* Python 3.11+
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn
* Passlib (bcrypt)
* Python-Jose (JWT)

---

## 🔐 Funcionalidades

### 👤 Autenticação

* Registro de usuário
* Login com geração de token JWT

### 📋 Tarefas

* Criar tarefa
* Listar tarefas do usuário autenticado
* Atualizar tarefa (marcar como concluída)
* Deletar tarefa

---

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas.git
cd task-api
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

---

### 3. Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 5. Rodar o servidor

```bash
uvicorn app.main:app --reload
```

---

### 6. Acessar documentação

```
http://127.0.0.1:8000/docs
```

---

## 🔑 Autenticação

Para acessar rotas protegidas:

1. Faça login em `/login`
2. Copie o token retornado
3. Clique em **Authorize** no Swagger
4. Insira:

```
Bearer SEU_TOKEN_AQUI
```

---

## 📡 Endpoints principais

| Método | Rota        | Descrição          |
| ------ | ----------- | ------------------ |
| POST   | /register   | Criar usuário      |
| POST   | /login      | Autenticar usuário |
| POST   | /tasks      | Criar tarefa       |
| GET    | /tasks      | Listar tarefas     |
| PUT    | /tasks/{id} | Atualizar tarefa   |
| DELETE | /tasks/{id} | Deletar tarefa     |

---

## 🔒 Segurança

* Senhas criptografadas com bcrypt
* Autenticação via JWT
* Proteção de rotas com Bearer Token
* Isolamento de dados por usuário

---

## 📈 Melhorias futuras

* Paginação de tarefas
* Filtros por status
* Deploy em produção (Render/Railway)
* Integração com frontend (React)

---

## 👨‍💻 Autor

Desenvolvido por **brunin417.me**

---

## ⭐ Observação

Este projeto foi desenvolvido com foco em aprendizado e prática de desenvolvimento backend com autenticação, seguindo boas práticas de mercado.
