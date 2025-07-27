import datetime
import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base

if TYPE_CHECKING:
    from models import Role


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
        unique=True
    )
    password_hash: Mapped[str]
    name: Mapped[str]
    role_id: Mapped[int] = mapped_column(
        ForeignKey('role.id')
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    role: Mapped['Role'] = relationship(
        back_populates='users'
    )
