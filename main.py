from fastapi import FastAPI

from bookings.router import router as router_bookings
from users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
