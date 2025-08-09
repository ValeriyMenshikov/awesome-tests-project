from typing import NamedTuple
import pytest
import uuid


class UserData(NamedTuple):
    login: str
    email: str
    password: str


@pytest.fixture
def user() -> UserData:
    return UserData(
        login=str(uuid.uuid4()),
        email=str(uuid.uuid4()) + "@mail.ru",
        password="1234567890",
    )
