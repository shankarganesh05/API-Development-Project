from fastapi import FastAPI,status,Response,HTTPException,Depends
from pydantic import BaseModel
from . import model
from .database import engine
from sqlmodel import SQLModel
from .routers import post,user,auth

# Create FastAPI instance
app = FastAPI()
# Create the database tables

SQLModel.metadata.create_all(engine)
# Pydantic model for Post

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
# Root endpoint
@app.get("/")
def get_root():
    return {"message": "Welcome to the FastAPI Project!"}