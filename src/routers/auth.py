from fastapi import FastAPI,status,Response,HTTPException,Depends,APIRouter
from sqlmodel import select,Session
from ..database import get_session
from .. import model,schemas,utils

router = APIRouter(tags=['Authentication'])

@router.post("/login")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_session)):
    user = db.exec(select(model.Users).filter(model.Users.email == user_credentials.email)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    return {"token": "example_token"}



