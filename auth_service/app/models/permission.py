from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class Permission(Base):
    """Модель разрешения."""

    __tablename__ = 'permission'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    code: Mapped[str] = mapped_column(
        String(128),
        unique=True
    )
    description: Mapped[str]