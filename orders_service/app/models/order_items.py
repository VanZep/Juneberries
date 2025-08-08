import uuid
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .orders import Order


class OrderItem(Base):
    """Модель позиции заказа."""

    __tablename__ = 'order_items'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    order_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('orders.id')
    )
    product_id: Mapped[uuid.UUID]
    quantity: Mapped[int]
    unit_price: Mapped[Decimal]

    order: Mapped['Order'] = relationship(
        back_populates='items'
    )
