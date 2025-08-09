from framework.fixtures.data.user import UserData
from framework.helpers.account import AccountHelper


def test_post_user_register(account_helper: AccountHelper, user: UserData) -> None:
    """
    Test register user
    """
    login = user.login
    email = user.email
    password = user.password

    account_helper.register_user(login=user.login, email=email, password=password)
    user_info = account_helper.user_info(login=user.login, password=password)
    assert user_info.resource.login == login
