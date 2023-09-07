from datetime import date
from typing import Optional

from fastapi import APIRouter

from exception import (
    CheckOutEarlierThanCheckIn,
    TooLongBookingPeriod,
)
from hotels.schemas import SchemaHotels
from hotels.service import HotelsService

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/id/{hotel_id}")
async def get_hotel_by_id(hotel_id: int) -> Optional[SchemaHotels]:
    return await HotelsService.get_by_id(hotel_id)


@router.get("/{location}")
async def get_hotel_by_location(
    location: str, check_in_date: date, check_out_date: date
) -> list[SchemaHotels]:
    if check_in_date > check_out_date:
        raise CheckOutEarlierThanCheckIn
    if (check_out_date - check_in_date).days > 28:
        raise TooLongBookingPeriod
    return await HotelsService.get_all(location, check_in_date, check_out_date)
