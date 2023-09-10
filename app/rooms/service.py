from app.rooms.models import Rooms
from app.service.base import BaseService


class RoomsService(BaseService):
    model = Rooms
