from fastapi import FastAPI

from bookings.router import router as router_bookings
from hotels.router import router as router_hotels
from rooms.router import router as router_rooms
from users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_rooms)
app.include_router(router_hotels)
