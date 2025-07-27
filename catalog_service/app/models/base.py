from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from config import settings


class Base(DeclarativeBase):
    """Базовая абстрактная модель."""

    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)