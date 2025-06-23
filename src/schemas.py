from pydantic import BaseModel,EmailStr
from typing import Optional


class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(Post):
    pass
class PostUpdate(Post):
    title: str
    content: str
    published: bool

class PostResponse(Post):
    title: str
    content: str
    published: bool
    id : int
    class Config:
        from_attributes = True
class UserCreate(BaseModel):
    email: EmailStr
    password: str
class UserResponse(BaseModel):
    email: EmailStr
    id: int
    class Config:
        from_attributes = True
class UserLogin(BaseModel):
    email: EmailStr
    password: str
class Token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id: Optional[int] = None