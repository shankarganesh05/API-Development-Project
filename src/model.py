from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime, text, Boolean
import datetime


class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    content: str = Field(nullable=False)
    published: bool = Field(sa_column=Column(Boolean,server_default = 'True',nullable=False))
    created_at: datetime.datetime = Field(sa_column=Column(DateTime(timezone=True),server_default=text('now()'),nullable=False))