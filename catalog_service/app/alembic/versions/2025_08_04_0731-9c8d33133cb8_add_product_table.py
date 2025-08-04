"""add product table

Revision ID: 9c8d33133cb8
Revises: d37e11eb7ece
Create Date: 2025-08-04 07:31:44.595269

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c8d33133cb8'
down_revision: Union[str, Sequence[str], None] = 'd37e11eb7ece'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'product',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('price', sa.Numeric(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('category_id', sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(['category_id'], ['category.id'], name=op.f('fk_product_category_id_category')),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_product')),
        sa.UniqueConstraint('id', name=op.f('uq_product_id'))
    )
    op.create_unique_constraint(op.f('uq_category_id'), 'category', ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f('uq_category_id'), 'category', type_='unique')
    op.drop_table('product')
