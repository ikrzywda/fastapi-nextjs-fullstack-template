from typing import AsyncGenerator

from sqlmodel import Session, create_engine

from app.core.config import settings

DB_ENGINE = create_engine(str(settings.POSTGRES_DB_URI))


async def get_session() -> AsyncGenerator[Session, None]:
    try:
        db = Session(DB_ENGINE)
        yield db
    finally:
        db.close()
