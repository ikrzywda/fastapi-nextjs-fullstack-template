from typing import Optional
from pydantic import BaseModel


class TodoItem(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    owner_id: int


class TodoItemCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    owner_id: int


class TodoItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoItemSearch(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
