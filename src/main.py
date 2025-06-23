from fastapi import FastAPI,status,Response,HTTPException,Depends
from pydantic import BaseModel
from . import model
from .database import get_session,engine
from sqlmodel import SQLModel,Session,select
from .routers import post,user

# Create FastAPI instance
app = FastAPI()
# Create the database tables

SQLModel.metadata.create_all(engine)
# Pydantic model for Post

app.include_router(post.router)
app.include_router(user.router)
# Root endpoint
@app.get("/")
def get_root():
    return {"message": "Welcome to the FastAPI Project!"}
@app.get("/sqlmodel")
def test_sqlmodel(db: Session = Depends(get_session)):
    post = db.exec(select(model.Post)).all()
    return {"message": post}