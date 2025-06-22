from fastapi import FastAPI,status,Response,HTTPException,Depends
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

# Create FastAPI instance
app = FastAPI()
# Pydantic model for Post
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
# Database connection
while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='fastapi',
            user='postgres',
            password='postgres',
            cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection successful")
        break
    except Exception as error:
        print("Database connection failed")
        print(f"Error: {error}")

# Root endpoint
@app.get("/")
def get_root():
    return {"message": "Welcome to the FastAPI Project!"}
# Getting all posts
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM post""")
    posts = cursor.fetchall()
    return {"data": posts}
# Getting a single post by id
@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM post WHERE id = %s""", (id,))
    post = cursor.fetchone()
    if post:
        return {"data": post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
# Creating a new post 
@app.post("/post", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    print(post.title, post.content, post.published)
    cursor.execute(""" INSERT INTO post (title,content,published) VALUES (%s,%s,%s) RETURNING * """, (post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}
# Deleting a post by id
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(""" DELETE FROM post WHERE id = %s RETURNING * """, (id,))
    del_post = cursor.fetchone()
    conn.commit()
    if del_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
    return {"message": f"Post with id {id} deleted successfully"}
# Updating a post by id
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute(""" UPDATE post SET title = %s,content = %s,published = %s WHERE id = %s RETURNING * """, (post.title,post.content,post.published,id))
    upd_post = cursor.fetchone()
    conn.commit()
    if upd_post:
        return {"message": f"Post with id {id} updated successfully", "data": upd_post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")