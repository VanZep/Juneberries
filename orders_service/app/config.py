from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseModel):
    """Настройки приложения."""

    title: str = 'Orders Service'
    summary: str = 'Заказы'
    description: str = '''
        - Проверка цен из Catalog Service
        - Сохранение заказа в БД, учитывая то, что цены товаров в валюте,
        а итоговая сумма заказа в рублях
        - Отправка событий ORDER_CREATED; ORDER_UPDATED в Kafka
        Стек: FastAPI + SQLAlchemy + PostgreSQL + Kafka
        БД: PostgreSQL Kafka: отправка события ORDER_CREATED
        '''


class RunConfig(BaseModel):
    """Настройки запуска uvicorn."""

    app: str = 'main:app'
    host: str = '127.0.0.1'
    port: int = 8000
    reload: bool = False


class ApiPrefix(BaseModel):
    """Настройки API префиксов."""

    prefix: str = '/api'
    v1: str = '/v1'
    orders: str = '/orders'


class DatabaseConfig(BaseModel):
    """Настройки PostgreSQL."""

    user: str
    password: str
    host: str
    port: int
    name: str

    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        'ix': 'ix_%(column_0_label)s',
        'uq': 'uq_%(table_name)s_%(column_0_N_name)s',
        'ck': 'ck_%(table_name)s_%(constraint_name)s',
        'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
        'pk': 'pk_%(table_name)s'
    }

    @property
    def url(self) -> PostgresDsn:
        """Формирование URL подключения БД."""
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
        env_prefix='ORDERS_SERVICE__'
    )
    app: AppConfig = AppConfig()
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()
