from datetime import datetime
from enum import Enum, unique
from typing import Literal, Optional

from pydantic import BaseModel
from sqlmodel import Column, DateTime, Field, ForeignKey, SQLModel

from app.models.base_model import BaseDBModel


class TodoItemCreate(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    due_date: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True)), default=None
    )


class TodoItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    is_completed: Optional[bool] = None


class TodoItem(BaseDBModel, table=True):
    __tablename__ = "todo_item"
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    due_date: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True)), default=None
    )
    todo_list_id: Optional[int] = Field(
        default=None,
        sa_column=Column(ForeignKey("todo_list.id", ondelete="CASCADE")),
    )
    created_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )
    updated_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )


TodoItemSortingFields = Literal["id", "title", "created_date", "updated_date"]
