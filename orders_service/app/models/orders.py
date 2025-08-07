import uuid
from decimal import Decimal
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import UUID, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .order_items import OrderItem


class Order(Base):
    """Модель заказа."""

    __tablename__ = 'orders'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    user_id: Mapped[uuid.UUID]
    total_price: Mapped[Decimal]
    cart_price: Mapped[Decimal]
    delivery_price: Mapped[Decimal]
    status: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    items: Mapped[list['OrderItem']] = relationship(
        back_populates='order',
        cascade='all, delete'
    )
