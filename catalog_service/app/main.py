import uvicorn
from  fastapi import FastAPI

from config import settings

app = FastAPI(
    title='Catalog Service',
    summary='Товары и категории',
    description='''
    - CRUD для товаров и категорий
    - Кеширование списка категорий в Redis
    - При изменении товара отправляется событие PRODUCT_UPDATED в Kafka
    - Цены товаров в каталоге указаны в валюте
    Стек: FastAPI + SQLAlchemy + Alembic + PostgreSQL + Redis + Kafka
    БД: PostgreSQL Redis: кеширование списка категорий 
    (categories_list, TTL = 1 час)
    Kafka: при обновлении товара → PRODUCT_UPDATED')
    '''
)

if __name__ == '__main__':
    uvicorn.run(
        app=settings.run.app,
        host=settings.run.host,
        port=settings.run.port,
        reload=(settings.run.reload, True),
    )