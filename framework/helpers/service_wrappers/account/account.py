from framework.internal.clients.http.account_api.apis.account_api import AccountApi
from framework.internal.clients.http.account_api.models.api_models import (
    UserDetailsEnvelope,
    DeleteAccountAccountDeleteResponse200,
)


class AccountApiClient(AccountApi):
    def user_info(self, token: str) -> UserDetailsEnvelope:
        return self.get_account_info(token=token)

    def delete_user(
        self, token: str, email: str
    ) -> DeleteAccountAccountDeleteResponse200:
        return self.delete_account(token=token, email=email)
