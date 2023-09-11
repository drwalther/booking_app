from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
)

from app.config import (
    DB_URI,
    MODE,
    TEST_DB_URI,
)

if MODE == "TEST":
    DATABASE_URI = TEST_DB_URI
    BD_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URI = DB_URI
    DB_PARAMS = {}

engine = create_async_engine(DATABASE_URI, **DB_PARAMS)

session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
