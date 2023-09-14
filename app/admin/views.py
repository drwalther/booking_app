from sqladmin import ModelView

from app.bookings.models import Bookings
from app.rooms.models import Rooms
from app.users.models import Users


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    column_searchable_list = [Users.email]
    page_size = 50
    page_size_options = [50, 100, 200]
    column_labels = {Users.email: "Email", Users.id: "ID пользователя"}
    icon = "fa-solid fa-user"


class BookingsAdmin(ModelView, model=Bookings):
    column_list = "__all__"
    name = "Бронирование"
    name_plural = "Бронирования"
    column_searchable_list = [Bookings.user]
    page_size = 50
    page_size_options = [50, 100, 200]
    column_labels = {
        Bookings.user: "Пользователь",
        Bookings.user_id: "ID Пользователя",
        Bookings.check_in_date: "Дата заезда",
        Bookings.check_out_date: "Дата выезда",
        Bookings.total_cost: "Стоимость",
        Bookings.total_days: "Всего дней",
        Bookings.price: "Цена",
        Bookings.room: "Номер",
        Bookings.room_id: "ID номера",
    }
    icon = "fa-solid fa-book"


class RoomsAdmin(ModelView, model=Rooms):
    column_list = "__all__"
    name = "Номер"
    name_plural = "Номера"
    column_searchable_list = [Rooms.hotel, Rooms.services]
    page_size = 50
    page_size_options = [50, 100, 200]
    column_labels = {
        Rooms.room_name: "Номер",
        Rooms.hotel: "Отель",
        Rooms.services: "Услуги",
        Rooms.rooms_quantity: "Количество номеров",
        Rooms.description: "Описание",
        Rooms.hotel_id: "ID отеля",
        Rooms.price: "Цена",
    }
    icon = "fa-solid fa-bed"
