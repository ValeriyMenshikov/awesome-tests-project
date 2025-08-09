from framework.internal.clients.http.register_api import AccountApi
from framework.internal.clients.http.register_api.models.api_models import (
    Registration,
    RegisterUserRegisterPostResponse201,
    UserEnvelope,
)


class RegisterApiClient(AccountApi):
    def register(
        self, login: str, email: str, password: str
    ) -> RegisterUserRegisterPostResponse201:
        response = self.post_user_register(
            registration=Registration(
                login=login,
                email=email,
                password=password,
            )
        )
        return response

    def activate(self, token: str) -> UserEnvelope:
        return self.put_user_activate(token=token)
