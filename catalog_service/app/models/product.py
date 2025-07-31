import uuid
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import UUID, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base

if TYPE_CHECKING:
    from models import Category


class Product(Base):
    """Модель товара."""

    __tablename__ = 'product'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    name: Mapped[str]
    price: Mapped[Decimal]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    category_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('category.id')
    )

    category: Mapped['Category'] = relationship(
        back_populates='products'
    )
