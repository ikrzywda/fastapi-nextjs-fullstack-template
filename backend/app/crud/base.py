from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from sqlmodel import SQLModel, Session
from result import Result

T = TypeVar("T")
Model = TypeVar("Model", bound=SQLModel)
CreateSchema = TypeVar("CreateSchema")
UpdateSchema = TypeVar("UpdateSchema")
SearchSchema = TypeVar("SearchSchema")


class PaginationResult(Generic[T]):
    def __init__(
        self, items: list[T], *, page_size: int, page_number: int, total: int
    ) -> None:
        self.items = items
        self.page_size = page_size
        self.page_number = page_number
        self.total = total


class CRUDError(Exception):
    pass


class CRUDBase(ABC, Generic[Model, CreateSchema, UpdateSchema, SearchSchema]):
    def __init__(self, session: Session) -> None:
        self.session = session

    @abstractmethod
    def get(self, id: int) -> Result[Model, CRUDError]:
        return

    @abstractmethod
    def create(self, obj_in: CreateSchema) -> Result[Model, CRUDError]:
        return

    @abstractmethod
    def update(self, id: int, obj_in: UpdateSchema) -> Result[Model, CRUDError]:
        return

    @abstractmethod
    def delete(self, id: int) -> Result[None, CRUDError]:
        return

    @abstractmethod
    def paginate(
        self, page_size: int, page_number: int, search: SearchSchema
    ) -> Result[PaginationResult[Model], CRUDError]:
        return
