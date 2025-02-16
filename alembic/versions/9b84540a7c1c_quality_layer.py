"""quality_layer

Revision ID: 9b84540a7c1c
Revises: 463161aec4ec
Create Date: 2025-02-08 14:22:48.518703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b84540a7c1c'
down_revision: Union[str, None] = '463161aec4ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pycon_prices', sa.Column('market', sa.String(length=32), nullable=True))
    op.create_unique_constraint('unique_date_equity_id_market', 'pycon_prices', ['date', 'equity_id', 'market'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_date_equity_id_market', 'pycon_prices', type_='unique')
    op.drop_column('pycon_prices', 'market')
    # ### end Alembic commands ###
