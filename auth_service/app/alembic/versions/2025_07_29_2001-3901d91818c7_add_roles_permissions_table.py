"""add roles_permissions table

Revision ID: 3901d91818c7
Revises: 9b6401a1eea3
Create Date: 2025-07-29 20:01:44.884210

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3901d91818c7'
down_revision: Union[str, Sequence[str], None] = '9b6401a1eea3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'roles_permissions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.Column('permission_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['permission_id'], ['permission.id'], name=op.f('fk_roles_permissions_permission_id_permission')),
        sa.ForeignKeyConstraint(['role_id'], ['role.id'], name=op.f('fk_roles_permissions_role_id_role')),
        sa.PrimaryKeyConstraint('id', 'role_id', 'permission_id', name=op.f('pk_roles_permissions'))
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('roles_permissions')
