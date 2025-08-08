"""add order_items table

Revision ID: adf7d2b51ce0
Revises: b66db4d928f7
Create Date: 2025-08-07 13:48:17.471204

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'adf7d2b51ce0'
down_revision: Union[str, Sequence[str], None] = 'b66db4d928f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'order_items',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('order_id', sa.UUID(), nullable=False),
        sa.Column('product_id', sa.Uuid(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('unit_price', sa.Numeric(), nullable=False),
        sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name=op.f('fk_order_items_order_id_orders')),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_order_items')),
        sa.UniqueConstraint('id', name=op.f('uq_order_items_id'))
    )
    op.create_unique_constraint(op.f('uq_orders_id'), 'orders', ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f('uq_orders_id'), 'orders', type_='unique')
    op.drop_table('order_items')
