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

    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    """Настройки проекта."""

    model_config = SettingsConfigDict(
        env_file='.env',
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix='APP_CONFIG__'
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    # db: DatabaseConfig


settings = Settings()
