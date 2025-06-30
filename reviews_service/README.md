# Reviews Service

## Назначение:
- Сохранение и редактирование отзывов по товарам
- Может отправлять событие REVIEW_CREATED в Kafka (review_events)
- Используется индекс по product_id для быстрого выборки

### Технологии:
Python 3.11, FastAPI, SQLAlchemy, Alembic, MongoDB (PyMongo/Motor), Kafka (опционально)