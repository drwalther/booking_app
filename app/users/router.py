from fastapi import (
    APIRouter,
    Depends,
    Response,
)

from app.exception import (
    UserAlreadyExistsException,
    UserDoesNotExistException,
)
from app.tasks.tasks import send_registration_confirmation_email
from app.users.auth import (
    authenticate_user,
    create_access_token,
    get_password_hash,
)
from app.users.helpers import get_current_user
from app.users.models import Users
from app.users.schemas import SchemaUserAuth
from app.users.service import UsersService

router = APIRouter(prefix="/auth", tags=["Auth and users"])


@router.post("/register")
async def register_user(user_data: SchemaUserAuth):
    existing_user = await UsersService.get_one(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException()
    hashed_password = get_password_hash(user_data.password)
    await UsersService.add(email=user_data.email, hashed_password=hashed_password)
    send_registration_confirmation_email.delay(user_data.email)


@router.post("/login")
async def login_user(response: Response, user_data: SchemaUserAuth):
    user = await authenticate_user(email=user_data.email, password=user_data.password)
    if not user:
        raise UserDoesNotExistException()
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")


@router.get("/me")
async def get_me(current_user: Users = Depends(get_current_user)):
    return {"email": current_user.email, "user id": current_user.id}
