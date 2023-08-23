from fastapi import (
    HTTPException,
    status,
)


class CustomException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(CustomException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class UserDoesNotExistException(CustomException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User doesn't exists"


class TokenIncorrectException(CustomException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token incorrect"


class TokenExpiredException(CustomException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token expired"


class TokenNotFoundException(CustomException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token not found"


class InvalidTokenException(CustomException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Invalid token"


class UserNotFoundException(CustomException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Internal error"
