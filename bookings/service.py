from bookings.models import Bookings
from service.base import BaseService


class BookingsService(BaseService):
    model = Bookings
