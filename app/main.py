from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.bookings.router import router as router_bookings
from app.hotels.router import router as router_hotels
from app.rooms.router import router as router_rooms
from app.users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_rooms)
app.include_router(router_hotels)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)
