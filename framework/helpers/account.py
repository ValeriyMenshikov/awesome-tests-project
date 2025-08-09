from framework.helpers.service_wrappers.account.account import AccountApiClient
from framework.helpers.service_wrappers.auth.auth import AuthApiClient
from framework.helpers.service_wrappers.mail.mail import MailApiClient
from framework.helpers.service_wrappers.register.register import RegisterApiClient
from framework.internal.clients.http.register_api.models.api_models import UserEnvelope


class AccountHelper:
    def __init__(
        self,
        register_client: RegisterApiClient,
        account_client: AccountApiClient,
        auth_client: AuthApiClient,
        mail_client: MailApiClient,
    ):
        self.register_client = register_client
        self.account_client = account_client
        self.auth_client = auth_client
        self.mail_client = mail_client

    def register_user(self, login: str, email: str, password: str) -> UserEnvelope:
        self.register_client.register(login, email, password)
        token = self.mail_client.search_confirmation_token(email)
        activation_response = self.register_client.activate(token=token)
        return activation_response
