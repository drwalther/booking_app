from datetime import (
    datetime,
    timedelta,
)

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import (
    ALGORITHM,
    SECRET_KEY,
)
from app.users.service import UsersService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersService.get_one(email=email)
    if not (user and verify_password(password, user.hashed_password)):
        return None
    return user


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
