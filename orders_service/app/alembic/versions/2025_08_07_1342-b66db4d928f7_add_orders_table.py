"""add orders table

Revision ID: b66db4d928f7
Revises: 
Create Date: 2025-08-07 13:42:21.497332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b66db4d928f7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'orders',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('user_id', sa.Uuid(), nullable=False),
        sa.Column('total_price', sa.Numeric(), nullable=False),
        sa.Column('cart_price', sa.Numeric(), nullable=False),
        sa.Column('delivery_price', sa.Numeric(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_orders')),
        sa.UniqueConstraint('id', name=op.f('uq_orders_id'))
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('orders')
