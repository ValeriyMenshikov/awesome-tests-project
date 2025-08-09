from framework.internal.clients.http.auth_api import AuthApi
from framework.internal.clients.http.auth_api.models.api_models import (
    LoginCredentials,
    UserEnvelope,
    LogoutAuthLogoutDeleteResponse200,
)


class AuthApiClient(AuthApi):
    def auth(
        self, login: str, password: str, remember_me: bool = False
    ) -> UserEnvelope:
        return self.post_auth_auth(
            login_credentials=LoginCredentials(
                login=login, password=password, remember_me=remember_me
            )
        )

    def logout(self, token: str) -> LogoutAuthLogoutDeleteResponse200:
        return self.delete_auth_logout(token=token)
