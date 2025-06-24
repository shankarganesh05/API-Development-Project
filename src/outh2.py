import jwt
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from typing import Dict
from datetime import datetime,timedelta,timezone
from jwt.exceptions import InvalidTokenError
from . import schemas
from .config import settings
outh2_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY=settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expires_minutes

def create_token(data:Dict):
    to_encode=data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str,crendiatials_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id :str = payload.get("user_id")
        if id is None:
            raise crendiatials_exception
        token_data = schemas.TokenData(id=id)
    except InvalidTokenError:
        raise crendiatials_exception
    return token_data

def get_current_user(token:str = Depends(outh2_scheme)):
    crendiatials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate Crendiatials",headers={"WWW-Authenticate": "Bearer"})
    return verify_token(token,crendiatials_exception)
