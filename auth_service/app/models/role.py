from typing import Literal, List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from models.mixins import IdIntPrimaryKeyMixin

if TYPE_CHECKING:
    from models import User, Permission

Role_name = Literal['user', 'manager', 'admin']


class Role(IdIntPrimaryKeyMixin, Base):
    """Модель роли пользователя."""

    __tablename__ = 'role'

    name: Mapped[Role_name]
    description: Mapped[str | None]

    users: Mapped[List['User']] = relationship(
        back_populates='role'
    )

    permissions: Mapped[List['Permission']] = relationship(
        secondary='role_permission',
        back_populates='roles'
    )