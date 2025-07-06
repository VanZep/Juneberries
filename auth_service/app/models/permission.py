from typing import List, TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from models.mixins import IdIntPrimaryKeyMixin

if TYPE_CHECKING:
    from models import Role


class Permission(IdIntPrimaryKeyMixin, Base):
    """Модель разрешения."""

    __tablename__ = 'permission'

    code: Mapped[str] = mapped_column(
        String(128),
        unique=True
    )
    description: Mapped[str]

    roles: Mapped[List['Role']] = relationship(
        secondary='role_permission',
        back_populates='permissions'
    )