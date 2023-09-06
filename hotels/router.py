from datetime import date

from fastapi import APIRouter

from hotels.schemas import SchemaHotels
from hotels.service import HotelsService

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/id/{hotel_id}")
async def get_hotel_by_id(hotel_id: int) -> SchemaHotels:
    return await HotelsService.get_by_id(hotel_id)


@router.get("/{location}")
async def get_hotel_by_location(
    location: str, check_in_date: date, check_out_date: date
) -> list[SchemaHotels]:
    return await HotelsService.get_all(location, check_in_date, check_out_date)
