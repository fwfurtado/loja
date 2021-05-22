"""add name column of customer

Revision ID: f72fad229571
Revises: 2be110d333f1
Create Date: 2021-05-22 11:56:21.799583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f72fad229571'
down_revision = '2be110d333f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('name', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customers', 'name')
    # ### end Alembic commands ###
