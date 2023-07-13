from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class Todo(TodoBase):
    id: int
    completed_on: Optional[datetime] = None
    created_on: datetime


class TodoDBModel(TodoBase, SQLModel, table=True):
    __tablename__ = "todos"
    # sequence as primary key,
    # more info at
    # https://sqlmodel.tiangolo.com/tutorial/automatic-id-none-refresh/
    id: Optional[int] = Field(default=None, primary_key=True)
    created_on: datetime = Field(default_factory=datetime.utcnow)
