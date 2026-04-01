from passlib.context import CryptContext
from jose import jwt 
from datetime import datetime, timedelta


SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash da senha
def hash_password(password: str):
    # evita erro de limite do bcrypt
    password = password.encode('utf-8')
    return pwd_context.hash(password[:72])
 
# Verificação da senha
def verify_password(plain, hashed):
    plain = plain.encode('utf-8')
    return pwd_context.verify(plain[:72], hashed)

# Criar token JWT
def create_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=1)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)