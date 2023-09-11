import asyncio
import json

import pytest
from sqlalchemy import insert

from app.bookings.models import Bookings
from app.config import MODE
from app.database import (
    Base,
    engine,
    session_maker,
)
from app.hotels.models import Hotels
from app.rooms.models import Rooms
from app.users.models import Users


@pytest.fixture(scope="session", autouse=True)
async def prepare_db():
    """Creates testing environment."""
    assert MODE == "TEST"

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

        def open_mock(model: str):
            with open(f"app/tests/mock_{model}.json", "r") as file:
                return json.load(file)

        hotels = open_mock("hotels")
        rooms = open_mock("rooms")
        users = open_mock("rooms")
        bookings = open_mock("bookings")

        async with session_maker() as session:
            add_hotels = insert(Hotels).values(hotels)
            add_rooms = insert(Rooms).values(rooms)
            add_users = insert(Users).values(users)
            add_bookings = insert(Bookings).values(bookings)

            await session.execute(add_hotels)
            await session.execute(add_rooms)
            await session.execute(add_users)
            await session.execute(add_bookings)
            await session.commit()

    @pytest.fixture(scope="session")
    def event_loop(request):
        """Code from pytest-asyncio documentation.

        Creates an instance of the default event loop for each test
        case.
        """
        loop = asyncio.get_event_loop_policy().new_event_loop()
        yield loop
        loop.close()