from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

if settings.MODE == "TEST":
    DATABASE_URI = settings.TEST_DB_URI
    DB_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URI = settings.DB_URI
    DB_PARAMS = {}

engine = create_async_engine(DATABASE_URI, **DB_PARAMS)

session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass
