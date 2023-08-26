from datetime import date

from sqlalchemy import (
    and_,
    func,
    insert,
    or_,
    select,
)

from bookings.models import Bookings
from database import session_maker
from rooms.models import Rooms
from service.base import BaseService


class BookingsService(BaseService):
    model = Bookings

    @classmethod
    async def add(
        cls, user_id: int, room_id: int, check_in_date: date, check_out_date: date
    ):
        async with session_maker() as session:
            booked_rooms = (
                select(Bookings)
                .where(
                    and_(
                        Bookings.room_id == 1,
                        or_(
                            and_(
                                Bookings.check_in_date >= check_out_date,
                                Bookings.check_in_date <= check_out_date,
                            ),
                            and_(
                                Bookings.check_in_date <= check_out_date,
                                Bookings.check_out_date > check_in_date,
                            ),
                        ),
                    )
                )
                .cte("booked_rooms")
            )

            get_rooms_left = (
                select(
                    (Rooms.rooms_quantity - func.count(booked_rooms.c.room_id)).label(
                        "rooms_left"
                    )
                )
                .select_from(Rooms)
                .join(booked_rooms, booked_rooms.c.room_id == Rooms.id)
                .where(Rooms.id == 1)
                .group_by(Rooms.rooms_quantity, booked_rooms.c.room_id)
            )

            rooms_left = await session.execute(get_rooms_left)
            rooms_left: int = rooms_left.scalar()

            if rooms_left > 0:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()
                add_booking = (
                    insert(Bookings)
                    .values(
                        user_id=user_id,
                        check_in_date=check_in_date,
                        check_out_date=check_out_date,
                        price=price,
                    )
                    .returning(Bookings)
                )

                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()
            else:
                return None
