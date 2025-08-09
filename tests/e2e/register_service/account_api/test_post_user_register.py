from framework.fixtures.data.user import UserData
from framework.helpers.account import AccountHelper


def test_post_user_register(account_helper: AccountHelper, user: UserData) -> None:
    account_helper.register_user(
        login=user.login, email=user.email, password=user.password
    )
