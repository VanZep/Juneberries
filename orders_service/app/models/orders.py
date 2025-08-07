import uuid
from decimal import Decimal
from datetime import datetime

from sqlalchemy import UUID, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Order(Base):
    """Модель заказа."""

    __tablename__ = 'orders'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('users.id')
    )
    total_price: Mapped[Decimal]
    cart_price: Mapped[Decimal]
    delivery_price: Mapped[Decimal]
    status: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
