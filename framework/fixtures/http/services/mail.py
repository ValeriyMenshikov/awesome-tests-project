import pytest
from restcodegen.restclient import Client, Configuration

from framework.config.settings import Settings
from framework.helpers.service_wrappers.mail.mail import MailApiClient


@pytest.fixture(scope="session")
def mail_service_api_client(settings: Settings) -> Client:
    configuration = Configuration(base_url=settings.mail_api_url)
    return Client(configuration)


@pytest.fixture(scope="session")
def mail_api(mail_service_api_client: Client) -> MailApiClient:
    return MailApiClient(api_client=mail_service_api_client)
