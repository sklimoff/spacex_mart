from functools import lru_cache

from pydantic_settings import BaseSettings

__ALL__ = ['config']


class Config(BaseSettings):
    postgres_host: str = 'localhost'
    postgres_port: int = 25432
    postgres_user: str = 'student'
    postgres_password: str = 'str0ng_p455w0rd'
    postgres_db: str = 'spacex_db'

    def get_postgres_dsn(self) -> str:
        return f'postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}'  # noqa: E501


@lru_cache
def get_config() -> Config:
    return Config()


config = get_config()
