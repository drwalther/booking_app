from fastapi import APIRouter

from bookings.service import BookingsService

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.get("")
async def get_bookings():
    return await BookingsService.get_all()
