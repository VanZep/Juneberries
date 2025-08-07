import uuid
from datetime import datetime
from typing import List, TYPE_CHECKING

from sqlalchemy import UUID, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base

if TYPE_CHECKING:
    from models import Product


class Category(Base):
    """Модель категории."""

    __tablename__ = 'categories'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    products: Mapped[List['Product']] = relationship(
        back_populates='category'
    )
