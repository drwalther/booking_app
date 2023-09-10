from pydantic import (
    BaseModel,
    EmailStr,
)


class SchemaUserAuth(BaseModel):
    email: EmailStr
    password: str
