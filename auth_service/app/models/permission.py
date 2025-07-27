from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base

if TYPE_CHECKING:
    from models import Role


class Permission(Base):
    """Модель разрешения."""

    __tablename__ = 'permission'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    code: Mapped[str] = mapped_column(
        unique=True
    )
    description: Mapped[str]

    roles: Mapped[List['Role']] = relationship(
        secondary='roles_permissions',
        back_populates='permissions'
    )
