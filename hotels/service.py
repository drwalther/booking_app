from datetime import date

from sqlalchemy import (
    and_,
    func,
    or_,
    select,
)

from bookings.models import Bookings
from database import session_maker
from hotels.models import Hotels
from rooms.models import Rooms
from service.base import BaseService


class HotelsService(BaseService):
    model = Hotels

    @classmethod
    async def get_all(cls, location: str, check_in_date: date, check_out_date: date):
        booked_rooms = (
            select(Bookings.room_id, func.count(Bookings.room_id).label("rooms_booked"))
            .select_from(Bookings)
            .where(
                or_(
                    and_(
                        Bookings.check_in_date >= check_in_date,
                        Bookings.check_in_date <= check_out_date,
                    ),
                    and_(
                        Bookings.check_in_date <= check_in_date,
                        Bookings.check_out_date > check_in_date,
                    ),
                ),
            )
            .group_by(Bookings.room_id)
            .cte("booked_rooms")
        )

        booked_hotels = (
            select(
                Rooms.hotel_id,
                func.sum(
                    Rooms.rooms_quantity - func.coalesce(booked_rooms.c.rooms_booked, 0)
                ).label("rooms_left"),
            )
            .select_from(Rooms)
            .join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True)
            .group_by(Rooms.hotel_id)
            .cte("booked_hotels")
        )

        get_hotels_with_rooms = (
            select(
                Hotels.__table__.columns,
                booked_hotels.c.rooms_left,
            )
            .join(booked_hotels, booked_hotels.c.hotel_id == Hotels.id, isouter=True)
            .where(
                and_(
                    booked_hotels.c.rooms_left > 0,
                    Hotels.location.like(f"%{location}%"),
                )
            )
        )

        async with session_maker() as session:
            hotels_with_rooms = await session.execute(get_hotels_with_rooms)
            return hotels_with_rooms.mappings().all()
