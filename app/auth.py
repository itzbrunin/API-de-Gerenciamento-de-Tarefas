'''Módulo de autenticação para o FastAPI.
Responsável por hash de senhas, verificação,criação de tokens JWT e validação do usuário.
'''

from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials 

security = HTTPBearer()

# Configurações de segurança
SECRET_KEY = "supersecret" # Em produção usar variável de ambiente
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 1

# Configuração do bcrypt para hash de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Criptografar senha do usuário
def hash_password(password: str):
    """
    Gera hash da senha usando bcrypt.

    Observação:
    - bcrypt possui limite de 72 bytes
    - por isso fazemos encode + truncamento
    """
    password = password.encode('utf-8')
    return pwd_context.hash(password[:72])
 
# Verificação da senha informada no login
def verify_password(plain_password: str, hashed_password: str):
    """
    Compara senha digitada com hash armazenado no banco.
    """
    plain_password = plain_password.encode('utf-8')
    return pwd_context.verify(plain_password[:72], hashed_password)
    

# Criar token JWT
def create_token(data: dict):
    """
    Gera um token JWT com tempo de expiração.
    """
    if "sub" not in data:
        raise ValueError("Token precisa ter 'sub' (username)")
    
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Obter usuário autenticado a partir do token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Valida o token JWT e retorna o usuário autenticado.
    """
    try:
        token = credentials.credentials  # 👈 pega o token correto

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        return username

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")