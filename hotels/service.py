from hotels.models import Hotels
from service.base import BaseService


class HotelsService(BaseService):
    model = Hotels
