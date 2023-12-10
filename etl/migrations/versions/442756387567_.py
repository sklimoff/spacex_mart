"""empty message

Revision ID: 442756387567
Revises: 4e6681d3b44d
Create Date: 2023-12-10 13:09:21.984267
"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '442756387567'
down_revision: Union[str, None] = '4e6681d3b44d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'launch', 'details', existing_type=sa.VARCHAR(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'launch', 'details', existing_type=sa.VARCHAR(), nullable=False
    )
    # ### end Alembic commands ###
