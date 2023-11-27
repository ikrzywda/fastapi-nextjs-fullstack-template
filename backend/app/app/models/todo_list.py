from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel
from sqlmodel import Column, DateTime, Field, ForeignKey

from app.models.base_model import BaseDBModel


class TodoListCreate(BaseModel):
    title: str
    description: str


class TodoListUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class TodoList(BaseDBModel, table=True):
    __tablename__ = "todo_list"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(
        default=None, sa_column=Column(ForeignKey("user.id", ondelete="CASCADE"))
    )
    title: str
    description: str
    created_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )
    updated_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )


TodoListSortingFields = Literal["id", "title", "created_date", "updated_date"]
