from datetime import date

from fastapi import (
    APIRouter,
    Depends,
)
from pydantic import TypeAdapter
from starlette import status

from app.bookings.schemas import SchemaBooking
from app.bookings.service import BookingsService
from app.exception import RoomIsNotAvailable
from app.tasks.tasks import send_booking_confirmation_email
from app.users.helpers import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SchemaBooking]:
    return await BookingsService.get_all(user_id=user.id)


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_booking(
    room_id: int,
    check_in_date: date,
    check_out_date: date,
    user: Users = Depends(get_current_user),
):
    booking = await BookingsService.add(user.id, room_id, check_in_date, check_out_date)
    if not booking:
        raise RoomIsNotAvailable
    # converts booking to dict for Celery
    booking_to_dict = TypeAdapter(SchemaBooking).validate_python(booking).model_dump()

    send_booking_confirmation_email.delay(booking_to_dict, user.email)
    return booking_to_dict


@router.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_booking(booking_id: int, user: Users = Depends(get_current_user)):
    return await BookingsService.delete(user.id, booking_id)
