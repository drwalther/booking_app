from datetime import date
from typing import List

from fastapi import APIRouter

from app.rooms.schemas import SchemaRoomInfo
from app.rooms.service import RoomsService

# room is the subset of hotel and I use hotels prefix
router = APIRouter(prefix="/hotels", tags=["Rooms"])


@router.get("/{hotel_id}/rooms")
async def get_rooms(
    hotel_id: int, date_from: date, date_to: date
) -> List[SchemaRoomInfo]:
    rooms = await RoomsService.get_all(hotel_id, date_from, date_to)
    return rooms
