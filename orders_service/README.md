# Orders Service

## Назначение:
- Проверка цен из Catalog Service
- Сохранение заказа в БД, учитывая то, что цены товаров в валюте, а итоговая сумма заказа в рублях
- Отправка событий ORDER_CREATED; ORDER_UPDATED в Kafka
- БД: PostgreSQL Kafka: отправка события ORDER_CREATED

### Технологии:
Python 3.11, FastAPI, SQLAlchemy, Alembic, PostgreSQL, Kafka