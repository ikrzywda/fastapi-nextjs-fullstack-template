from enum import Enum
from typing import Generic, List, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel
from sqlmodel import SQLModel

ModelType = TypeVar("ModelType", bound=BaseModel | SQLModel)


class SortingOrder(str, Enum):
    asc = "asc"
    desc = "desc"


class PaginatedResponse(GenericModel, Generic[ModelType]):
    total: int
    page: int
    per_page: int
    items: List[ModelType]
