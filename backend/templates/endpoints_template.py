from fastapi import APIRouter, Depends, HTTPException

from app import models, schemas

router = APIRouter()


@router.get("/todo-items/{id}")
async def get_todo_item(
    id: int,
    db: Session = Depends(get_db),
) -> schemas.TodoItem:
    """
    Get a todo item by id.
    """
    todo_item = crud.todo_item.get(db, id=id)
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return todo_item
