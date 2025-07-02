import datetime
import uuid

from sqlalchemy import UUID, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from base import Base


class User(Base):
    """Модель пользователя."""

    __tablename__ = 'user'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4(),
        unique=True
    )
    email: Mapped[str] = mapped_column(
        String(254),
        unique=True
    )
    password_hash: Mapped[str] = mapped_column(
        String(256)
    )
    name: Mapped[str] = mapped_column(
        String(50)
    )
    role_id: Mapped[int] = mapped_column(
        ForeignKey('role.id')
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )