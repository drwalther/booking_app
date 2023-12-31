from datetime import date

from sqlalchemy import (
    and_,
    delete,
    func,
    insert,
    or_,
    select,
)

from app.bookings.models import Bookings
from app.database import session_maker
from app.rooms.models import Rooms
from app.service.base import BaseService


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
                        Bookings.room_id == room_id,
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
                .join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True)
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
                        room_id=room_id,
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

    @classmethod
    async def delete(cls, user_id: int, booking_id: int):
        async with session_maker() as session:
            query = delete(Bookings).filter_by(id=booking_id, user_id=user_id)
            await session.execute(query)
            await session.commit()
