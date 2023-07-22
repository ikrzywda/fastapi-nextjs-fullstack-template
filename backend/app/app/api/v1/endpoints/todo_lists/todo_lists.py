from typing import Optional

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.db import get_session
from app.crud.crud_todo_list import crud_todo_list
from app.dependencies.auth import get_current_user
from app.models.todo_list import TodoList, TodoListCreate, TodoListSortingFields
from app.models.user import User
from app.schamas.paginated_response import PaginatedResponse, SortingOrder

router = APIRouter()


@router.post("", response_model=TodoList)
async def create_todo_list(
    todo_list_in: TodoListCreate,
    db_session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
) -> TodoList:
    todo_list = crud_todo_list.create_for_user(
        db=db_session, obj_in=todo_list_in, user_id=user.id
    )
    return todo_list


@router.get("", response_model=PaginatedResponse[TodoList])
async def get_todo_lists(
    page: int = 1,
    page_size: int = 10,
    search: Optional[str] = None,
    sorting_order: SortingOrder = SortingOrder.asc,
    sorting_key: TodoListSortingFields = TodoListSortingFields.id,
    db_session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
) -> PaginatedResponse[TodoList]:
    return crud_todo_list.get_for_user_paginated(
        db_session,
        page=page,
        per_page=page_size,
        search=search,
        user_id=user.id,
        sorting_key=sorting_key,
        sorting_order=sorting_order,
    )
