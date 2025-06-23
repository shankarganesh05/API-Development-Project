from fastapi import FastAPI,status,Response,HTTPException,Depends,APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select,Session
from ..database import get_session
from .. import model,schemas,utils,outh2

router = APIRouter(tags=['Authentication'])

@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_session)):
    user = db.exec(select(model.Users).filter(model.Users.email == user_credentials.username)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    access_token = outh2.create_token(data={"user_id":user.id})
    return {"access_token": access_token,"token_type": "bearer"}



