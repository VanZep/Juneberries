"""add permissions table

Revision ID: c12d12053b50
Revises: b8b0b06b1630
Create Date: 2025-08-04 12:34:03.117933

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c12d12053b50'
down_revision: Union[str, Sequence[str], None] = 'b8b0b06b1630'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'permissions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('code', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_permissions')),
        sa.UniqueConstraint('code', name=op.f('uq_permissions_code'))
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('permissions')
