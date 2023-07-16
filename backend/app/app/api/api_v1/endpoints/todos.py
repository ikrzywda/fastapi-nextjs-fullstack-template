from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.models.todo import Todo, TodoCreate
from sqlmodel import Session

from app.core.db import get_session
from app import crud


router = APIRouter()


@router.post("", response_model=Todo)
async def create_todo(
    todo_in: TodoCreate,
    db_session: Session = Depends(get_session),
) -> Todo:
    todo = crud.todo.create(db=db_session, obj_in=todo_in)
    return todo


@router.get("", response_model=List[Todo])
async def get_todo(
    db_session: Session = Depends(get_session),
) -> List[Todo]:
    todos = crud.todo.get_multi(db=db_session, skip=0, limit=100)
    return todos


@router.patch("/{todo_id}", response_model=Todo)
async def update_todo(
    todo_id: int,
    todo_in: TodoCreate,
    db_session: Session = Depends(get_session),
) -> Todo:
    todo = crud.todo.get(db=db_session, id=todo_id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")

    todo = crud.todo.update(db=db_session, db_obj=todo, obj_in=todo_in)
    return todo


@router.delete("/{todo_id}", response_model=None)
async def delete_todo(
    todo_id: int,
    db_session: Session = Depends(get_session),
) -> None:
    crud.todo.remove(db=db_session, id=todo_id)
    return None
