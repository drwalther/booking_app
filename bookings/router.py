from fastapi import (
    APIRouter,
    Depends,
)

from bookings.schemas import SchemaBooking
from bookings.service import BookingsService
from users.helpers import get_current_user
from users.models import Users

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SchemaBooking]:
    return await BookingsService.get_all(user_id=user.id)
