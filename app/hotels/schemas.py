from typing import List

from pydantic import BaseModel


class SchemaHotels(BaseModel):
    services: List[str]
    id: int
    name: str
    location: str
    room_quantity: int
    image_id: int

    class Config:
        from_attributes = True
