"""add roles table

Revision ID: b8b0b06b1630
Revises: 
Create Date: 2025-08-04 12:28:29.383755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8b0b06b1630'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Enum('user', 'manager', 'admin', native_enum=False), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_roles'))
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('roles')
