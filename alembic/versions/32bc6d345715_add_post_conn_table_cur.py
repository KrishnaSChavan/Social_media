"""add post conn table cur

Revision ID: 32bc6d345715
Revises: 2e011e32c9eb
Create Date: 2023-05-17 23:51:49.592577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32bc6d345715'
down_revision = '2e011e32c9eb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
