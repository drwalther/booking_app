from fastapi import HTTPException
from passlib.context import CryptContext
from pydantic import EmailStr

from users.service import UsersService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def login_user(email: EmailStr, password: str):
    user = await UsersService.get_one(email=email)
    if not user and not verify_password(password, user.password):
        raise HTTPException(
            status_code=409, detail="User is not exists or password is incorrect"
        )
    return user
