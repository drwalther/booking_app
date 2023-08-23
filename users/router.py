from fastapi import (
    APIRouter,
    HTTPException,
    Response,
    status,
)

from users.auth import (
    authenticate_user,
    create_access_token,
    get_password_hash,
)
from users.schemas import SchemaUserAuth
from users.service import UsersService

router = APIRouter(prefix="/auth", tags=["Auth and users"])


@router.post("/register")
async def register_user(user_data: SchemaUserAuth):
    existing_user = await UsersService.get_one(email=user_data.email)
    if existing_user:
        # it seems more correct than code 422
        raise HTTPException(status_code=409, detail="User already exists")
    hashed_password = get_password_hash(user_data.password)
    await UsersService.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SchemaUserAuth):
    user = await authenticate_user(email=user_data.email, password=user_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User doesn't exists"
        )
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")
