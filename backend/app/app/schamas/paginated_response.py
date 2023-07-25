from enum import Enum
from typing import Generic, List, TypeVar

from pydantic.generics import GenericModel
from app.models.base_model import BaseDBModel


ModelType = TypeVar("ModelType", bound=BaseDBModel, covariant=True)


class SortingOrder(str, Enum):
    asc = "asc"
    desc = "desc"


class PaginatedResponse(GenericModel, Generic[ModelType]):
    total: int
    page: int
    per_page: int
    items: List[ModelType]
