import pytest
from restcodegen.restclient import Client, Configuration

from framework.config.settings import Settings
from framework.helpers.service_wrappers.users.users import UsersApiClient


@pytest.fixture(scope="session")
def api_client(settings: Settings) -> Client:
    configuration = Configuration(base_url=settings.users_api_url)
    return Client(configuration)


@pytest.fixture(scope="session")
def users_api(api_client: Client) -> UsersApiClient:
    return UsersApiClient(api_client=api_client)
