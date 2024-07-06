from pydantic import Field
from pydantic_settings import BaseSettings
from os import environ

class Settings(BaseSettings):
    DB_URL: str = Field(default=f'postgresql+asyncpg://{environ['POSTGRES_USER']}:{environ['POSTGRES_PASSWORD']}@localhost:{environ['POSTGRES_PORT']}/{environ['POSTGRES_DB']}')


settings = Settings()