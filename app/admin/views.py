from sqladmin import ModelView

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
