from fastapi import FastAPI
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

from app.admin.views import (
    BookingsAdmin,
    HotelsAdmin,
    RoomsAdmin,
    UsersAdmin,
)
from app.bookings.router import router as router_bookings
from app.database import engine
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

# Admin panel for DB
admin = Admin(app, engine)
admin.add_view(UsersAdmin)
admin.add_view(BookingsAdmin)
admin.add_view(RoomsAdmin)
admin.add_view(HotelsAdmin)
