from app.crud.base import CRUDBase
from app.models.todo_item import TodoItem, TodoItemCreate, TodoItemUpdate


class CRUDTodoItem(CRUDBase[TodoItem, TodoItemCreate, TodoItemUpdate]):
    pass


crud_todo_item = CRUDTodoItem(TodoItem)
