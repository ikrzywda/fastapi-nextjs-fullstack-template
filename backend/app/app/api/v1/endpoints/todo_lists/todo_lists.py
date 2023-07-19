from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.todo_list import TodoList, TodoListCreate
from app.core.db import get_session
from app.crud.crud_todo_list import crud_todo_list

router = APIRouter()


@router.post("", response_model=TodoList)
async def create_todo_list(
    todo_list_in: TodoListCreate,
    db_session: Session = Depends(get_session),
) -> TodoList:
    todo_list = crud_todo_list.create_for_user(
        db=db_session, obj_in=todo_list_in, user_id=user.id
    )
    return todo_list
