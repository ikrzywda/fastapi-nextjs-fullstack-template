from typing import Optional
from sqlmodel import Field, SQLModel


class TodoItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    completed: bool = False
    owner_id: int
