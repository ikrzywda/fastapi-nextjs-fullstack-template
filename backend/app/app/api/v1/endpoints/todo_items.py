from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.models.todo_item import TodoItem, TodoItemCreate
from sqlmodel import Session

from app.core.db import get_session
from app.crud.crud_todo_item import crud_todo_item


router = APIRouter()


@router.post("", response_model=TodoItem)
async def create_todo(
    todo_in: TodoItemCreate,
    db_session: Session = Depends(get_session),
) -> TodoItem:
    todo = crud_todo_item.create(db=db_session, obj_in=todo_in)
    return todo


@router.get("", response_model=List[TodoItem])
async def get_todo(
    db_session: Session = Depends(get_session),
) -> List[TodoItem]:
    todos = crud_todo_item.get_multi(db=db_session, skip=0, limit=100)
    return todos


@router.patch("/{todo_id}", response_model=TodoItem)
async def update_todo(
    todo_id: int,
    todo_in: TodoItemCreate,
    db_session: Session = Depends(get_session),
) -> TodoItem:
    todo = crud_todo_item.get(db=db_session, id=todo_id)

    if not todo:
        raise HTTPException(status_code=404, detail="TodoItem item not found")

    todo = crud_todo_item.update(db=db_session, db_obj=todo, obj_in=todo_in)
    return todo


@router.delete("/{todo_id}", response_model=None)
async def delete_todo(
    todo_id: int,
    db_session: Session = Depends(get_session),
) -> None:
    crud.todo_item.remove(db=db_session, id=todo_id)
    return None
