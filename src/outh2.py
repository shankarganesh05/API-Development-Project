import jwt
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from typing import Dict
from datetime import datetime,timedelta
from jwt.exceptions import InvalidTokenError
from . import schemas
outh2_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_token(data:Dict):
    to_encode=data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
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

    