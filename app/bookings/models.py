from sqlalchemy import (
    Column,
    Computed,
    Date,
    ForeignKey,
    Integer,
)

from app.database import Base


class Bookings(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey("rooms.id"))
    user_id = Column(ForeignKey("users.id"))
    check_in_date = Column(Date, nullable=False)
    check_out_date = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed("(check_out_date - check_in_date) * price"))
    total_days = Column(Integer, Computed("check_out_date - check_in_date"))
