from core.config import settings
from sqlmodel import Session, create_engine

DB_ENGINE = create_engine(settings.POSTGRES_DB_URI)


async def get_session():
    print(settings.POSTGRES_DB_URI)
    with Session(DB_ENGINE) as session:
        yield session
