from fastapi import FastAPI,status,Response,HTTPException,Depends,APIRouter
from typing import List
from ..database import get_session
from .. import model,schemas,utils
from sqlmodel import select,Session

router = APIRouter(prefix="/users",tags=['Users'])

@router.get("/",response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_session)):
    users = db.exec(select(model.Users)).all()
    return users
@router.post("/signup",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate,db: Session = Depends(get_session)):
    new_user = model.Users(**user.model_dump())
    new_user.password = utils.hash(user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@router.get("/{id}",response_model=schemas.UserResponse)
def get_user(id:int,db: Session = Depends(get_session)):
    user = db.get(model.Users, id)
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")
