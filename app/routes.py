from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@router.post("/tasks")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    
    # Cria uma nova tarefa no banco de dados
    # Parâmetros:
    # -task: dados da tarefa enviados pelo usuário
    # - db: sessão do banco de dados
    # Retorna: - A tarefa criada
    
    new_task = models.Task(title=task.title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# READ
@router.get("/tasks")
def list_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

# UPDATE
@router.put("/tasks/{task_id}")
def update_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).get(task_id)
    if task:
        task.completed = True
        db.commit()
    return task

# DELETE
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).get(task_id)
    if task:
        db.delete(task)
        db.commit()
    return {"msg": "Deletado"}