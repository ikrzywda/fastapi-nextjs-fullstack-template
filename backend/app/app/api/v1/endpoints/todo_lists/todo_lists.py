from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
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


@router.delete("/{todo_list_id}", response_model=None)
async def delete_todo_list(
    todo_list_id: int,
    db_session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
) -> None:
    todo_list = crud_todo_list.get(db_session, id=todo_list_id)

    if not todo_list:
        raise HTTPException(
            status_code=404,
            detail="Todo list not found",
        )

    if todo_list.user_id != user.id:
        raise HTTPException(
            status_code=403,
            detail="You don't have permissions to delete this todo list",
        )

    crud_todo_list.remove_for_user(db_session, id=todo_list_id)
    return None
