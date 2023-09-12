import asyncio
import json
from datetime import datetime

import pytest
from httpx import AsyncClient
from sqlalchemy import insert

from app.bookings.models import Bookings
from app.config import MODE
from app.database import (
    Base,
    engine,
    session_maker,
)
from app.hotels.models import Hotels
from app.main import app as fastapi_app
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
            """Reads mock data."""
            with open(f"app/tests/mock_{model}.json", encoding="utf-8") as file:
                return json.load(file)

        hotels = open_mock("hotels")
        rooms = open_mock("rooms")
        users = open_mock("users")
        bookings = open_mock("bookings")

        for booking in bookings:
            booking["check_in_date"] = datetime.strptime(
                booking["check_in_date"], "%Y-%m-%d"
            )
            booking["check_out_date"] = datetime.strptime(
                booking["check_out_date"], "%Y-%m-%d"
            )

        async with session_maker() as session:
            for Model, values in [
                (Hotels, hotels),
                (Rooms, rooms),
                (Users, users),
                (Bookings, bookings),
            ]:
                query = insert(Model).values(values)
                await session.execute(query)

            await session.commit()


@pytest.fixture(scope="session")
def event_loop(request):
    """Code from pytest-asyncio documentation.

    Creates an instance of the default event loop for each test case.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def async_client():
    """Creates async client for endpoints."""
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac
