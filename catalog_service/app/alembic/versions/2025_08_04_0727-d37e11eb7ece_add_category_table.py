"""add category table

Revision ID: d37e11eb7ece
Revises: 
Create Date: 2025-08-04 07:27:05.500313

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd37e11eb7ece'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'category',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_category')),
        sa.UniqueConstraint('id', name=op.f('uq_category_id'))
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('category')
