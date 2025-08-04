from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class RolesPermissions(Base):
    """Промежуточная модель для связи роли и разрешения пользователя."""

    __tablename__ = 'roles_permissions'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    role_id: Mapped[int] = mapped_column(
        ForeignKey('roles.id'),
        primary_key=True
    )
    permission_id: Mapped[int] = mapped_column(
        ForeignKey('permissions.id'),
        primary_key=True
    )
