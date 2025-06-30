# Auth Service

## Назначение:
- Регистрация и вход пользователей
- Выдача/обновление access и refresh токенов
- Middleware для проверки JWT в других сервисах
- Хранение токенов может использовать Redis (refresh, blacklisting).
- Поддержка ролей: user, manager, admin

### Технологии:
Python 3.11, FastAPI, SQLAlchemy, Alembic, PostgreSQL, JWT, Redis (для refresh токенов)