from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class TodoBase(BaseModel):
    title: str
    description: str | None = None


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None


class Todo(
    TodoBase,
    SQLModel,
    table=True,
):
    __tablename__ = "todos"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_on: datetime = Field(default_factory=datetime.utcnow)
