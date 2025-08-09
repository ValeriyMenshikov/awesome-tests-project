import pytest
from restcodegen.restclient import Client, Configuration

from framework.config.settings import Settings
from framework.helpers.service_wrappers.register.register import RegisterApiClient


@pytest.fixture(scope="session")
def users_service_api_client(settings: Settings) -> Client:
    configuration = Configuration(base_url=settings.register_api_url)
    return Client(configuration)


@pytest.fixture(scope="session")
def register_api(users_service_api_client: Client) -> RegisterApiClient:
    return RegisterApiClient(api_client=users_service_api_client)
