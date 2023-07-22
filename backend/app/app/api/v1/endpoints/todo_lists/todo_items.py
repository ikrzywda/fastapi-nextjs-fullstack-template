from typing import Optional

from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from app.core.db import get_session
from app.crud.crud_todo_item import crud_todo_item
from app.crud.crud_todo_list import crud_todo_list
from app.dependencies.auth import get_current_user
from app.models.todo_item import (
    TodoItem,
    TodoItemCreate,
    TodoItemSortingFields,
    TodoItemUpdate,
)
from app.models.user import User
from app.schamas.paginated_response import PaginatedResponse, SortingOrder

router = APIRouter()


@router.post("/{todo_list_id}/items", response_model=TodoItem)
async def create_todo_item(
    todo_list_id: int,
    todo_item_in: TodoItemCreate,
    db_session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
) -> TodoItem:
    todo_list = crud_todo_list.get_for_user(
        db_session, id=todo_list_id, user_id=user.id
    )

    if not todo_list:
        raise HTTPException(
            status_code=404,
            detail="Todo list not found",
        )

    return crud_todo_item.create_for_list(
        db=db_session, obj_in=todo_item_in, todo_list_id=todo_list_id
    )


@router.get("/{todo_list_id}/items", response_model=PaginatedResponse[TodoItem])
async def get_todo_items(
    todo_list_id: int,
    page: int = 1,
    page_size: int = 10,
    search: Optional[str] = None,
    sorting_order: SortingOrder = SortingOrder.asc,
    sorting_key: TodoItemSortingFields = TodoItemSortingFields.id,
    db_session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
) -> PaginatedResponse[TodoItem]:
    todo_list = crud_todo_list.get_for_user(
        db_session, id=todo_list_id, user_id=user.id
    )

    if not todo_list:
        raise HTTPException(
            status_code=404,
            detail="Todo list not found",
        )

    return crud_todo_item.get_for_list_paginated(
        db_session,
        page=page,
        per_page=page_size,
        search=search,
        todo_list_id=todo_list_id,
        sorting_key=sorting_key,
        sorting_order=sorting_order,
    )


@router.patch("/{todo_list_id}/items/{todo_item_id}", response_model=TodoItem)
async def update_todo_item(
    todo_list_id: int,
    todo_item_id: int,
    todo_item_in: TodoItemUpdate,
    db_session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
) -> TodoItem:
    todo_list = crud_todo_list.get_for_user(
        db_session, id=todo_list_id, user_id=user.id
    )

    if not todo_list:
        raise HTTPException(
            status_code=404,
            detail="Todo list not found",
        )

    todo_item = crud_todo_item.get(db_session, id=todo_item_id)

    if not todo_item:
        raise HTTPException(
            status_code=404,
            detail="Todo item not found",
        )

    return crud_todo_item.update(db_session, db_obj=todo_item, obj_in=todo_item_in)


@router.delete("/{todo_list_id}/items/{todo_item_id}", response_model=None)
async def delete_todo_item(
    todo_list_id: int,
    todo_item_id: int,
    db_session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
) -> None:
    todo_list = crud_todo_list.get_for_user(
        db_session, id=todo_list_id, user_id=user.id
    )

    if not todo_list:
        raise HTTPException(
            status_code=404,
            detail="Todo list not found",
        )

    todo_item = crud_todo_item.get(db_session, id=todo_item_id)

    if not todo_item:
        raise HTTPException(
            status_code=404,
            detail="Todo item not found",
        )

    crud_todo_item.remove(db_session, id=todo_item_id)
    return None
