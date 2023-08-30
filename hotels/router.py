from fastapi import APIRouter

from hotels.schemas import SchemaHotels
from hotels.service import HotelsService

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/id/{hotel_id}")
async def get_hotel_by_id(hotel_id: int) -> SchemaHotels:
    return await HotelsService.get_by_id(hotel_id)
