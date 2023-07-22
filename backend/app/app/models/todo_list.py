from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Column, DateTime, Field, ForeignKey, SQLModel


class TodoListBase(SQLModel):
    title: str
    description: str


class TodoListCreate(TodoListBase):
    pass


class TodoListUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class TodoList(TodoListBase, table=True):
    __tablename__ = "todo_list"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(
        default=None, sa_column=Column(ForeignKey("user.id", ondelete="CASCADE"))
    )
    created_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )
    updated_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )


class TodoListSortingFields(str, Enum):
    id = "id"
    title = "title"
    created_date = "created_date"
    updated_date = "updated_date"
