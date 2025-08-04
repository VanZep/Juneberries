"""add roles_permissions table

Revision ID: 78396faac7b5
Revises: 88026abd334e
Create Date: 2025-08-04 12:38:21.983910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78396faac7b5'
down_revision: Union[str, Sequence[str], None] = '88026abd334e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'roles_permissions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.Column('permission_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['permission_id'], ['permissions.id'], name=op.f('fk_roles_permissions_permission_id_permissions')),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name=op.f('fk_roles_permissions_role_id_roles')),
        sa.PrimaryKeyConstraint('id', 'role_id', 'permission_id', name=op.f('pk_roles_permissions'))
    )
    op.create_unique_constraint(op.f('uq_users_id'), 'users', ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f('uq_users_id'), 'users', type_='unique')
    op.drop_table('roles_permissions')
