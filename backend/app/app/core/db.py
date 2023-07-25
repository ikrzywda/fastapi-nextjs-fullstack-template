from typing import AsyncGenerator, Optional
from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings

DB_ENGINE = create_engine(str(settings.POSTGRES_DB_URI))


class BaseDBModel(SQLModel):
    id: Optional[int]


async def get_session() -> AsyncGenerator[Session, None]:
    try:
        db = Session(DB_ENGINE)
        yield db
    finally:
        db.close()
