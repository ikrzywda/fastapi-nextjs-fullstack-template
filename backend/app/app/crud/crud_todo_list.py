from crud import CRUDBase

from app.models.todo_list import TodoList, TodoListCreate, TodoListUpdate


class CrudTodoList(CRUDBase[TodoList, TodoListCreate, TodoListUpdate]):
    def create_for_user(self, db, *, obj_in: TodoListCreate, user_id: int) -> TodoList:
        todo_list = TodoList(**obj_in.dict(), user_id=user_id)
        db.add(todo_list)
        db.commit()
        db.refresh(todo_list)
        return todo_list


crud_todo_list = CrudTodoList(TodoList)
