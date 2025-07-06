from typing import Literal, List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base

if TYPE_CHECKING:
    from models import User

Role_name = Literal['user', 'manager', 'admin']


class Role(Base):
    """Модель роли пользователя."""

    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    name: Mapped[Role_name]
    description: Mapped[str | None]

    users: Mapped[List['User']] = relationship(
        back_populates='role'
    )