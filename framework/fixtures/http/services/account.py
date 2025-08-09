import pytest
from restcodegen.restclient import Client, Configuration

from framework.config.settings import Settings
from framework.helpers.service_wrappers.account.account import AccountApiClient


@pytest.fixture(scope="session")
def account_service_api_client(settings: Settings) -> Client:
    configuration = Configuration(base_url=settings.account_api_url)
    return Client(configuration)


@pytest.fixture(scope="session")
def account_api(account_service_api_client: Client) -> AccountApiClient:
    return AccountApiClient(api_client=account_service_api_client)
