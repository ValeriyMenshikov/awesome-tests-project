import pytest

from framework.config.settings import Settings


@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings()  # type: ignore
