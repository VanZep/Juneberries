from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    """Параметры запуска uvicorn."""

    app: str = 'main:app'
    host: str = '127.0.0.1'
    port: int = 8000
    reload: bool = False


class AppConfig(BaseModel):
    """Настройки приложения."""

    title: str = 'Catalog Service'
    summary: str = 'Товары и категории'
    description: str = '''
        - CRUD для товаров и категорий
        - Кеширование списка категорий в Redis
        - При изменении товара отправляется событие PRODUCT_UPDATED в Kafka
        - Цены товаров в каталоге указаны в валюте
        Стек: FastAPI + SQLAlchemy + Alembic + PostgreSQL + Redis + Kafka
        БД: PostgreSQL Redis: кеширование списка категорий 
        (categories_list, TTL = 1 час)
        Kafka: при обновлении товара → PRODUCT_UPDATED')
        '''


class ApiPrefix(BaseModel):
    """API префикс."""

    prefix: str = '/api'
    v1: str = '/v1'
    products: str = '/products'


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

    naming_convention: dict[str, str] = {
        'ix': 'ix_%(column_0_label)s',
        'uq': 'uq_%(table_name)s_%(column_0_N_name)s',
        'ck': 'ck_%(table_name)s_%(constraint_name)s',
        'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
        'pk': 'pk_%(table_name)s'
    }

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
    app: AppConfig = AppConfig()
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()
