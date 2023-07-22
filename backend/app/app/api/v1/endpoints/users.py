from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.user import User, UserCreate
from app.crud.crud_user import crud_user
from app.core.db import get_session

router = APIRouter()


@router.post("", response_model=User)
async def create_user(
    user_in: UserCreate,
    db_session: Session = Depends(get_session),
) -> User:
    user = crud_user.create(db=db_session, obj_in=user_in)
    return user


@router.delete("/{user_id}", response_model=None)
async def delete_user(
    user_id: int,
    db_session: Session = Depends(get_session),
) -> None:
    crud_user.remove(db=db_session, id=user_id)
    return None
