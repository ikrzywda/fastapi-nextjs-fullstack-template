from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.core.db import get_session

from models.todo import Todo, TodoCreate

router = APIRouter()


@router.post("", response_model=Todo)
async def create_todo(
    todo_in: TodoCreate,
    db_session: Session = Depends(get_session),
) -> Todo:
    todo = Todo(**todo_in.dict())
    db_session.add(todo)
    db_session.commit()
    db_session.refresh(todo)

    return todo


@router.get("", response_model=List[Todo])
async def get_todo(
    db_session: Session = Depends(get_session),
) -> List[Todo]:
    todos = db_session.exec(select(Todo)).unique().all()
    return todos


@router.patch("/{todo_id}", response_model=Todo)
async def update_todo(
    todo_id: int,
    todo_in: TodoCreate,
    db_session: Session = Depends(get_session),
) -> Todo:
    todo = db_session.exec(select(Todo).where(Todo.id == todo_id)).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")

    for key, value in todo_in.dict().items():
        setattr(todo, key, value)

    db_session.add(todo)
    db_session.commit()
    db_session.refresh(todo)

    return todo


@router.delete("/{todo_id}", response_model=None)
async def delete_todo(
    todo_id: int,
    db_session: Session = Depends(get_session),
) -> None:
    todo = db_session.exec(select(Todo).where(Todo.id == todo_id)).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")

    db_session.delete(todo)
    db_session.commit()

    return None
