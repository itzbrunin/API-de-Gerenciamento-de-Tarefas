'''Módulo de rotas para o FastAPI.
Responsável por Registrar usuários, autenticar, proteger rotas usando JWT e CRUD.'''

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database, auth
from app.auth import get_current_user

router = APIRouter()

# Conexão com o banco de dados
def get_db():
    """
    Cria uma sessão com o banco de dados.
    """
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Registrar Usuario
@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Cria um novo usuário.

    - Verifica se o username já existe
    - Criptografa a senha
    - Salva no banco
    """
    # Verifica se o usuário já existe
    existing_user = db.query(models.User).filter(
        models.User.username == user.username
        ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    # Criptografa a senha do usuário
    hashed = auth.hash_password(user.password)

    # Cria um novo usuário 
    new_user = models.User(username=user.username, password=hashed)
    
    db.add(new_user)
    db.commit()
    return {"msg": "Usuário criado com sucesso"}
 
# LOGIN
@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Autentica usuário e retorna token JWT.
    """

    db_user = db.query(models.User).filter(
        models.User.username == user.username
        ).first()
    
    # Credenciais inválidas  
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    
    # Gerar token
    token = auth.create_token(data={"sub": db_user.username})
    return {"access_token": token}  

# Criar tarefa (rota protegida)
@router.post("/tasks")
def create_task(
    task: schemas.TaskCreate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)):
    """
    Cria uma nova tarefa para o usuário autenticado.
    """
    # Busca usuário
    user = db.query(models.User).filter(
        models.User.username == current_user
        ).first()
    
    # Cria tarefa vinculada ao usuário
    new_task = models.Task(
        title=task.title, 
        owner_id=user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

# Listar tarefas do usuário autenticado
@router.get("/tasks")
def list_tasks(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    """
    Lista todas as tarefas do usuário autenticado.
    """
    user = db.query(models.User).filter(
        models.User.username == current_user
        ).first()
    
    return db.query(models.Task).filter(
        models.Task.owner_id == user.id
        ).all()
    
# Atualizar tarefa
@router.put("/tasks/{task_id}")
def update_task(
    task_id: int,  
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    """
    Atualiza uma tarefa do usuário autenticado.
    """
    # Busca usuário
    user = db.query(models.User).filter(
        models.User.username == current_user
    ).first()
    
    # Busca a tarefa correta
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.owner_id == user.id
    ).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
     
    task.completed = True
    db.commit()
    db.refresh(task)

    return task

# Deletar tarefa
@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,  
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    """
    Deleta uma tarefa do usuário autenticado.
    """
    user = db.query(models.User).filter(
        models.User.username == current_user
        ).first()
    
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.owner_id == user.id
        ).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
     
    db.delete(task)
    db.commit()

    return {"msg": "Tarefa deletada com sucesso"}