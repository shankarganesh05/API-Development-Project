from pydantic import BaseModel


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
