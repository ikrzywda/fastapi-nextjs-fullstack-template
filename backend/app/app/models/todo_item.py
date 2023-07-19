from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, ForeignKey, SQLModel, Column, DateTime


class TodoItemBase(SQLModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    due_date: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True)), default=None
    )


class TodoItemCreate(TodoItemBase):
    pass


class TodoItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    is_completed: Optional[bool] = None


class TodoItem(TodoItemBase, table=True):
    __tablename__ = "todo_item"
    id: Optional[int] = Field(default=None, primary_key=True)
    todo_list_id: Optional[int] = Field(
        default=None,
        sa_column=Column(ForeignKey("todo_list.id", ondelete="CASCADE")),
    )
    created_date: datetime = Field(
        sa_column=(DateTime(timezone=True)), default_factory=datetime.utcnow
    )
    updated_date: datetime = Field(
        sa_column=(DateTime(timezone=True)), default_factory=datetime.utcnow
    )
