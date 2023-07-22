from typing import Any, Dict, Generic, Optional, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlmodel import Session, SQLModel, func, select

from app.schamas.paginated_response import PaginatedResponse

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLModel model class
        * `schema`: A Pydantic (or SQLModel) class
        """
        self.model = model

    def get_order_by_expression(self, sorting_key: str, sorting_order: str) -> Any:
        if sorting_order == "asc":
            return getattr(self.model, sorting_key)
        return getattr(self.model, sorting_key).desc()

    def get(self, db: Session, id: Any) -> ModelType | None:
        return db.exec(select(self.model).where(self.model.id == id)).first()

    def get_paginated(
        self, db: Session, *, page: int, per_page: int
    ) -> PaginatedResponse[ModelType]:
        skip = (page - 1) * per_page
        items = db.exec(select(self.model).offset(skip).limit(per_page)).all()
        total = db.exec(select(func.count(self.model.id))).one()
        return PaginatedResponse[ModelType](
            total=total, page=page, per_page=per_page, items=items
        )

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: UpdateSchemaType | Dict[str, Any]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> Optional[ModelType]:
        obj = db.exec(select(self.model).where(self.model.id == id)).first()
        db.delete(obj)
        db.commit()
        return obj
