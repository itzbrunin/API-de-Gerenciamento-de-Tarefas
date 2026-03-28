"""
Arquivo principal da aplicação.

Responsável por:
- Inicializar a API
- Conectar com o banco de dados
- Registrar as rotas
"""

from fastapi import FastAPI
from app import models, database
from app.routes import router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"msg": "API funcionando 🚀"}