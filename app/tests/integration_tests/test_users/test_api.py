import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("register@user.com", "no_password", 201),
        ("reg@user.com", "no_password", 201),
        ("register@user.com", "nO_password", 409),
        ("register@user", "no_password", 422),
        ("register@user.44", "no_password", 422),
        ("qwerty", "no_password", 422),
        (12345, "no_password", 422),
    ],
)
async def test_register_user(email, password, status_code, async_client: AsyncClient):
    response = await async_client.post(
        "/auth/register", json={"email": email, "password": password}
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("test@test.com", "test", 200),
        ("vasya@yandx.com", "artem", 200),
        ("nouser@test.com", "no_password", 401),
    ],
)
async def test_login_user(email, password, status_code, async_client: AsyncClient):
    response = await async_client.post(
        "/auth/login", json={"email": email, "password": password}
    )
    assert response.status_code == status_code
