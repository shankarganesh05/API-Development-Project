from fastapi import FastAPI,status,Response,HTTPException,Depends,APIRouter
from typing import List
from ..database import get_session
from .. import model,schemas,outh2
from sqlmodel import select,Session

router = APIRouter(prefix="/posts",tags=['Posts'])

# Getting all posts
@router.get("/",response_model = List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_session),current_user:int=Depends(outh2.get_current_user)):
    posts = db.exec(select(model.Post)).all()
    return posts
# Getting a single post by id
@router.get("/{id}",response_model=schemas.PostResponse)
def get_post(id: int, db: Session = Depends(get_session),current_user:int=Depends(outh2.get_current_user)):
    post = db.get(model.Post, id)
    if post:
        if post.user_id!= current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorized to perform the action")
        return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
    
# Creating a new post 
@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate,db: Session = Depends(get_session),current_user:int=Depends(outh2.get_current_user)):
    
    new_post = model.Post(user_id=current_user.id,**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
# Deleting a post by id
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_session),current_user:int=Depends(outh2.get_current_user)):
    del_post = db.get(model.Post, id)
    if del_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
    if del_post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorized to perform the action")
    db.delete(del_post)
    db.commit()
    return {"message": f"Post with id {id} deleted successfully"}
# Updating a post by id
@router.put("/{id}",response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostUpdate,db: Session = Depends(get_session),current_user:int=Depends(outh2.get_current_user)):
    upd_post = db.get(model.Post, id)
    if upd_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
    if upd_post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorized to perform this action")
    # upd_data = post.model_dump(exclude_unset=True)
    upd_post.sqlmodel_update(post.model_dump())
    db.add(upd_post)
    db.commit()
    db.refresh(upd_post)    
    return upd_post