import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("register@user.com", "no_password", 201),
        ("register@user.com", "nO_password", 409),
        ("qwerty", "no_password", 422),
        (12345, "no_password", 422),
    ],
)
async def test_register_user(email, password, status_code, async_client: AsyncClient):
    response = await async_client.post(
        "/auth/register", json={"email": email, "password": password}
    )
    print(response.status_code)
    print(response)

    assert response.status_code == status_code
