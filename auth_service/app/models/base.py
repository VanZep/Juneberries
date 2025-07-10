from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Базовая абстрактная модель."""

    __abstract__ = True

    metadata = MetaData()