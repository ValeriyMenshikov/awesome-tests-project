import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            ensure_ascii=False,
        )
    ]
)

pytest_plugins = [
    "framework.fixtures.http.services.auth",
    "framework.fixtures.http.services.account",
    "framework.fixtures.http.services.mail",
    "framework.fixtures.http.services.register",
    "framework.fixtures.http.services.users",
    "framework.fixtures.account",
    "framework.fixtures.data.user",
    "framework.fixtures.base",
]
