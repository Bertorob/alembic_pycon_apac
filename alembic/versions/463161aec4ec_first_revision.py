"""first_revision

Revision ID: 463161aec4ec
Revises: 
Create Date: 2025-02-04 17:07:20.132441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '463161aec4ec'
down_revision: Union[str, None] = None

def upgrade() -> None:
    op.create_table('pycon_prices',
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('equity_id', sa.String(length=32), nullable=False),
    sa.Column('price', sa.Float(), nullable=False,),
    sa.Column('volume', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('date', 'equity_id')
    )

def downgrade() -> None:
    op.drop_table('pycon_prices')
