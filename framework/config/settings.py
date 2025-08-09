from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
ENV_FILE = PROJECT_ROOT / "local.env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE), env_file_encoding="utf-8", case_sensitive=True
    )

    register_api_url: str = Field(validation_alias="REGISTER_API_URL")
    account_api_url: str = Field(validation_alias="ACCOUNT_API_URL")
    auth_api_url: str = Field(validation_alias="AUTH_API_URL")
    mail_api_url: str = Field(validation_alias="MAIL_API_URL")
    users_api_url: str = Field(validation_alias="USERS_API_URL")
