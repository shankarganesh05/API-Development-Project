from sqlmodel import SQLModel, Field,Relationship
from sqlalchemy import Column, DateTime, text, Boolean
from typing import ClassVar
import datetime


class Users(SQLModel,table=True):
    __tablename__="users"
    email: str = Field(nullable=False,unique=True)
    password:str = Field(nullable=False)
    id: int = Field(default=None, primary_key=True)
    created_at: datetime.datetime = Field(sa_column=Column(DateTime(timezone=True),server_default=text('now()'),nullable=False))
class Post(SQLModel, table=True):
    __tablename__="post"
    id: int = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    content: str = Field(nullable=False)
    published: bool = Field(sa_column=Column(Boolean,server_default = 'True',nullable=False))
    created_at: datetime.datetime = Field(sa_column=Column(DateTime(timezone=True),server_default=text('now()'),nullable=False))
    user_id: int = Field(foreign_key="users.id",nullable=False,ondelete="CASCADE")
    user : Users = Relationship()
