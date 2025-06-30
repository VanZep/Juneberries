# Catalog Service

## Назначение:
- CRUD для товаров и категорий
- Кеширование списка категорий в Redis
- При изменении товара отправляется событие PRODUCT_UPDATED в Kafka
- Цены товаров в каталоге указаны в валюте
- БД: PostgreSQL
- Redis: кеширование списка категорий (categories_list, TTL = 1 час)
- Kafka: при обновлении товара → PRODUCT_UPDATED

### Технологии:
Python 3.11, FastAPI, SQLAlchemy, Alembic, PostgreSQL, Redis, Kafka
