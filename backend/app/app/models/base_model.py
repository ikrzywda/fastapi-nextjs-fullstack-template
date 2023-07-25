from typing import Any
from sqlmodel import SQLModel


class BaseDBModel(SQLModel):
    id: Any
