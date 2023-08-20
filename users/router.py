from fastapi import (
    APIRouter,
    HTTPException,
)

from users.auth import get_password_hash
from users.schemas import SchemaUserRegister
from users.service import UsersService

router = APIRouter(prefix="/auth", tags=["Auth and users"])


@router.post("/register")
async def register_user(user_data: SchemaUserRegister):
    existing_user = await UsersService.get_one(email=user_data.email)
    if existing_user:
        # it seems more correct than code 422
        raise HTTPException(status_code=409, detail="User already exists")
    hashed_password = get_password_hash(user_data.password)
    await UsersService.add(email=user_data.email, hashed_password=hashed_password)
