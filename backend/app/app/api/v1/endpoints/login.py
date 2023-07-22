from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from schamas.token import Token
from sqlmodel import Session

from app.core.config import settings
from app.core.db import get_session
from app.core.security import create_id_token
from app.crud.crud_user import crud_user
from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/access-token", response_model=Token)
def login_access_token(
    db: Session = Depends(get_session),
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud_user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=settings.ID_TOKEN_EXPIRATION_MINUTES)
    return Token(
        access_token=create_id_token(user.id, expires_delta=access_token_expires),
        token_type="bearer",
    )


@router.post("/login/test-token", response_model=User)
def test_token(current_user: User = Depends(get_current_user)) -> User:
    """
    Test access token
    """
    return current_user
