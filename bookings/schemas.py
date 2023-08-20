from datetime import date

from pydantic import BaseModel


class SchemaBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    check_in_date: date
    check_out_date: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        from_attributes = True
