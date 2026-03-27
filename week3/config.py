from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Config(BaseSettings):
    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 5433
    DB_NAME: str = "dedb"
    DB_USER: str = "deuser"
    DB_PASSWORD: str = "pass123"
