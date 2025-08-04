"""add products table

Revision ID: 73641dd97677
Revises: 8a521246703d
Create Date: 2025-08-04 13:10:58.423154

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '73641dd97677'
down_revision: Union[str, Sequence[str], None] = '8a521246703d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'products',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('price', sa.Numeric(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('category_id', sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name=op.f('fk_products_category_id_categories')),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_products')),
        sa.UniqueConstraint('id', name=op.f('uq_products_id'))
    )
    op.create_unique_constraint(op.f('uq_categories_id'), 'categories', ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f('uq_categories_id'), 'categories', type_='unique')
    op.drop_table('products')
