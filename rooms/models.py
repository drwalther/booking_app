from sqlalchemy import (
    JSON,
    Column,
    ForeignKey,
    Integer,
    String,
)

from database import Base


class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey("hotels.id"))
    room_name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)
