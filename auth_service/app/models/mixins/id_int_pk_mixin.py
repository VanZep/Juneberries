from sqlalchemy.orm import Mapped, mapped_column


class IdIntPrimaryKeyMixin:
    """Миксин с полем ID целочисленного типа."""

    id: Mapped[int] = mapped_column(
        primary_key=True
    )