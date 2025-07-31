"""add permission table

Revision ID: 9b6401a1eea3
Revises: daccdfe8b571
Create Date: 2025-07-27 22:06:33.287337

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b6401a1eea3'
down_revision: Union[str, Sequence[str], None] = 'daccdfe8b571'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'permission',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('code', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_permission')),
        sa.UniqueConstraint('code', name=op.f('uq_permission_code'))
    )
    op.create_unique_constraint(
        op.f('uq_user_id'), 'user', ['id']
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        op.f('uq_user_id'), 'user', type_='unique'
    )
    op.drop_table('permission')
