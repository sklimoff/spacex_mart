"""Data Mart

Revision ID: 9aa1a4a0f17a
Revises: c33ea3a87af2
Create Date: 2023-12-11 00:37:48.734596
"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '9aa1a4a0f17a'
down_revision: Union[str, None] = 'c33ea3a87af2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'data_mart',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('type', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('media_type_name', sa.String(), nullable=False),
        sa.Column('ref', sa.String(), nullable=False),
        sa.Column('count', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_mart')
    # ### end Alembic commands ###
