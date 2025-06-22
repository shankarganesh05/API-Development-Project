from fastapi import FastAPI,status,Response,HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
app = FastAPI()
my_posts = []

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    
def find_post(id: int):
    for index, post in enumerate(my_posts):
        if post['id'] == id:
            return post,index
    return None, None
@app.get("/")
def get_root():
    return {"message": "Hello, World!"}
@app.get("/posts")
def get_posts():
    return {"data": my_posts}
@app.get("/posts/{id}")
def get_post(id: int):
    post,index = find_post(id)
    if post:
        return {"data": post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
@app.post("/post", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.model_dump()  # Convert Pydantic model to dict
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    print(my_posts)
    return {"data": post_dict}
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post,index = find_post(id)
    if post:
        my_posts.pop(index)
        return {"message": f"Post with id {id} deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    post_data, index = find_post(id)
    if post_data:
        post_dict = post.model_dump()
        post_dict['id'] = id
        my_posts[index] = post_dict
        return {"message": f"Post with id {id} updated successfully", "data": post_dict}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")