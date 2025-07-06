from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models import Base
from models.mixins import IdIntPrimaryKeyMixin

class RolePermission(IdIntPrimaryKeyMixin, Base):
    """Промежуточная модель для связи роли и разрешения пользователя."""

    __tablename__ = 'role_permission'

    role_id: Mapped[int] = mapped_column(
        ForeignKey('role.id'),
        primary_key=True
    )
    permission_id: Mapped[int] = mapped_column(
        ForeignKey('permission.id'),
        primary_key=True
    )