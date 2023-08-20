from sqlalchemy import select

from database import session_maker


class BaseService:
    model = None

    @classmethod
    async def get_by_id(cls, model_id: int):
        async with session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_one(cls, **params):
        async with session_maker() as session:
            query = select(cls.model).filter_by(**params)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, **params):
        async with session_maker() as session:
            query = select(cls.model).filter_by(**params)
            result = await session.execute(query)
            return result.scalars().all()
