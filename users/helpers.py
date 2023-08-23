from datetime import datetime

from fastapi import (
    Depends,
    Request,
)
from jose import (
    JWTError,
    jwt,
)

from config import (
    ALGORITHM,
    SECRET_KEY,
)
from exception import (
    InvalidTokenException,
    TokenExpiredException,
    TokenIncorrectException,
    TokenNotFoundException,
    UserNotFoundException,
)
from users.service import UsersService


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenNotFoundException()
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except JWTError:
        raise TokenIncorrectException()
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException()
    user_id: str = payload.get("sub")
    if not user_id:
        raise InvalidTokenException()
    user = await UsersService.get_by_id(int(user_id))
    if not user:
        raise UserNotFoundException()
    return user
