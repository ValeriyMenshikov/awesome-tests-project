import pytest
from restcodegen.restclient import Client, Configuration

from framework.config.settings import Settings
from framework.helpers.service_wrappers.auth.auth import AuthApiClient


@pytest.fixture(scope="session")
def auth_service_api_client(settings: Settings) -> Client:
    configuration = Configuration(base_url=settings.auth_api_url)
    return Client(configuration)


@pytest.fixture(scope="session")
def auth_api(auth_service_api_client: Client) -> AuthApiClient:
    return AuthApiClient(api_client=auth_service_api_client)
