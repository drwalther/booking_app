from fastapi import APIRouter

from bookings.schemas import SchemaBooking
from bookings.service import BookingsService

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.get("")
async def get_bookings() -> list[SchemaBooking]:
    return await BookingsService.get_all()
