from result import Err, Ok, Result
from sqlmodel import Session, select
from app.crud import CRUDError, CRUDBase
from app import schemas, models

# Path: backend/templates/crud_template.py


class CRUDTodo(
    CRUDBase[
        models.TodoItem,
        schemas.TodoItemCreate,
        schemas.TodoItemUpdate,
        schemas.TodoItemSearch,
    ]
):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def get(self, id: int) -> Result[models.TodoItem, CRUDError]:
        obj = self.session.exec(
            select(models.TodoItem).where(models.TodoItem.id == id)
        ).first()
        if obj is None:
            return Err(CRUDError("Object not found"))
        return Ok(obj)

    def create(
        self, obj_in: schemas.TodoItemCreate
    ) -> Result[models.TodoItem, CRUDError]:
        obj = models.TodoItem(**obj_in.dict())
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return Ok(obj)

    def update(
        self, id: int, obj_in: schemas.TodoItemUpdate
    ) -> Result[models.TodoItem, CRUDError]:
        obj = self.get(id).unwrap_or_raise(CRUDError)
        for key, value in obj_in.dict(exclude_unset=True).items():
            setattr(obj, key, value)

        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return Ok(obj)

    def delete(self, id: int) -> Result[None, CRUDError]:
        obj = self.get(id).unwrap_or_raise(CRUDError)
        self.session.delete(obj)
        self.session.commit()
        return Ok(None)
