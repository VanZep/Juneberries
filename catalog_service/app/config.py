from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    """Параметры запуска uvicorn."""

    app: str = 'main:app'
    host: str = '127.0.0.1'
    port: int = 8000
    reload: bool = False


class ApiPrefix(BaseModel):
    """API префикс."""

    prefix: str = '/api'


class DatabaseConfig(BaseModel):
    """Подключение PostgreSQL."""

    user: str
    password: str
    host: str
    port: int
    name: str

    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    @property
    def url(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            path=self.name
        )


class Settings(BaseSettings):
    """Настройки сервиса."""

    model_config = SettingsConfigDict(
        env_file='../.env',
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix='CATALOG_SERVICE__'
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()
