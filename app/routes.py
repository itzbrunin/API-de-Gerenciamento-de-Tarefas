from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database, auth

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Registrar Usuario
@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Verifica se o usuário já existe
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    # Criptografa a senha do usuário
    hashed = auth.hash_password(user.password)
    # Cria um novo usuário 
    new_user = models.User(username=user.username, password=hashed)
    db.add(new_user)
    db.commit()
    return {"msg": "Usuário criado "}
 
# LOGIN
@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    
    token = auth.create_token(data={"sub": db_user.username})
    return {"access_token": token}  