from app.crud.base import CRUDBase


class CRUDTodo(
    CRUDBase[Todo, TodoCreate, TodoUpdate]
):
    pass
