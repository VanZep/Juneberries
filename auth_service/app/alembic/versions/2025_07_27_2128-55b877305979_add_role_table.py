"""add role table

Revision ID: 55b877305979
Revises: 
Create Date: 2025-07-27 21:28:19.672059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55b877305979'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'role',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Enum('user', 'manager', 'admin', native_enum=False), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_role'))
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('role')
