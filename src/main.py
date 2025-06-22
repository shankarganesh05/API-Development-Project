from fastapi import FastAPI,status,Response,HTTPException,Depends
from pydantic import BaseModel
from random import randrange
from . import model
from .database import get_session,engine
from sqlmodel import SQLModel,Session,select,update

# Create FastAPI instance
app = FastAPI()
# Create the database tables
SQLModel.metadata.create_all(engine)
# Pydantic model for Post
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

# Root endpoint
@app.get("/")
def get_root():
    return {"message": "Welcome to the FastAPI Project!"}
@app.get("/sqlmodel")
def test_sqlmodel(db: Session = Depends(get_session)):
    post = db.exec(select(model.Post)).all()
    return {"message": post}
# Getting all posts
@app.get("/posts")
def get_posts(db: Session = Depends(get_session)):
    posts = db.exec(select(model.Post)).all()
    return {"data": posts}
# Getting a single post by id
@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_session)):
    post = db.get(model.Post, id)
    if post:
        return {"data": post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
# Creating a new post 
@app.post("/post", status_code=status.HTTP_201_CREATED)
def create_post(post: Post,db: Session = Depends(get_session)):
    new_post = model.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}
# Deleting a post by id
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_session)):
    del_post = db.get(model.Post, id)
    if del_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
    db.delete(del_post)
    db.commit()
    return {"message": f"Post with id {id} deleted successfully"}
# Updating a post by id
@app.put("/posts/{id}")
def update_post(id: int, post: Post,db: Session = Depends(get_session)):
    upd_post = db.get(model.Post, id)
    if upd_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
    # upd_data = post.model_dump(exclude_unset=True)
    upd_post.sqlmodel_update(post.model_dump())
    db.add(upd_post)
    db.commit()
    db.refresh(upd_post)    
    return {"message": f"Post with id {id} updated successfully", "data": upd_post}
    