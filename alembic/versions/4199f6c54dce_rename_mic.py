"""rename mic

Revision ID: 4199f6c54dce
Revises: 9b84540a7c1c
Create Date: 2025-02-08 14:32:29.149542

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '4199f6c54dce'
down_revision: Union[str, None] = '9b84540a7c1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pycon_prices', sa.Column('mic', sa.String(length=32), nullable=True))
    op.drop_constraint('unique_date_equity_id_market', 'pycon_prices', type_='unique')
    op.create_unique_constraint('unique_date_equity_id_market', 'pycon_prices', ['date', 'equity_id', 'mic'])
    op.drop_column('pycon_prices', 'market')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pycon_prices', sa.Column('market', mysql.VARCHAR(length=32), nullable=True))
    op.drop_constraint('unique_date_equity_id_market', 'pycon_prices', type_='unique')
    op.create_unique_constraint('unique_date_equity_id_market', 'pycon_prices', ['date', 'equity_id', 'market'])
    op.drop_column('pycon_prices', 'mic')
    # ### end Alembic commands ###
