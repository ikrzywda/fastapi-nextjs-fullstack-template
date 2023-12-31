from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

from sqlmodel import Column, DateTime, Field, String
from app.models.base_model import BaseDBModel


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    is_superuser: bool = False


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class User(BaseDBModel, table=True):
    __tablename__ = "user"
    username: str = Field(sa_column=Column(String, unique=True))
    email: str = Field(sa_column=Column(String, unique=True))
    hashed_password: str = Field(sa_column=Column(String))
    is_superuser: bool = Field(default=False)
    id: Optional[int] = Field(default=None, primary_key=True)
    created_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )
    updated_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )
