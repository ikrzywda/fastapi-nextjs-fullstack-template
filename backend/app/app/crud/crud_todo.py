from app.crud.base import CRUDBase
from app.models.todo import Todo, TodoCreate, TodoUpdate


class CRUDTodo(CRUDBase[Todo, TodoCreate, TodoUpdate]):
    pass


todo = CRUDTodo(Todo)
