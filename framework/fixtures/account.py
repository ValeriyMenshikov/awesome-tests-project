import pytest
from framework.helpers.account import AccountHelper
from framework.helpers.service_wrappers.account.account import AccountApiClient
from framework.helpers.service_wrappers.auth.auth import AuthApiClient
from framework.helpers.service_wrappers.mail.mail import MailApiClient
from framework.helpers.service_wrappers.register.register import RegisterApiClient


@pytest.fixture(scope="session")
def account_helper(
    register_api: RegisterApiClient,
    account_api: AccountApiClient,
    auth_api: AuthApiClient,
    mail_api: MailApiClient,
) -> AccountHelper:
    return AccountHelper(
        register_client=register_api,
        account_client=account_api,
        auth_client=auth_api,
        mail_client=mail_api,
    )
