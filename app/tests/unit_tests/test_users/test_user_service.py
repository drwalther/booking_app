import pytest

from app.users.service import UsersService


@pytest.mark.parametrize(
    "user_id, email, is_exist",
    [
        (1, "test@test.com", True),
        (2, "vasya@yandx.com", True),
        (3, "test@test.com", False),
    ],
)
async def test_get_user_by_id(user_id, email, is_exist):
    user = await UsersService.get_by_id(user_id)

    if is_exist:
        assert user.id == user_id
        assert user.email == email
    else:
        assert user is None
