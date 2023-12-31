from sqlalchemy import (
    insert,
    select,
)

from app.database import session_maker


class BaseService:
    model = None

    @classmethod
    async def get_by_id(cls, model_id: int):
        async with session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_one(cls, **filters):
        async with session_maker() as session:
            query = select(cls.model).filter_by(**filters)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, **filters):
        async with session_maker() as session:
            query = select(cls.model).filter_by(**filters)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def add(cls, **data):
        async with session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
