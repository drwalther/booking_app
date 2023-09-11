from typing import List

from pydantic import BaseModel


class SchemaRoom(BaseModel):
    id: int
    hotel_id: int
    room_name: str
    description: str | None
    services: List[str]
    price: int
    rooms_quantity: int
    image_id: int

    class Config:
        from_attributes = True


class SchemaRoomInfo(SchemaRoom):
    total_cost: int
    rooms_left: int

    class Config:
        from_attributes = True
