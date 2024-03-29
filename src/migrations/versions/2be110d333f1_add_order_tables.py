"""add order tables

Revision ID: 2be110d333f1
Revises: 88359808368e
Create Date: 2021-05-22 10:31:41.772121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2be110d333f1'
down_revision = '88359808368e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.BigInteger(), nullable=False),
    sa.Column('payment_type', sa.Enum('ONLINE', 'BANK_SLIP', name='orderpaymenttype'), nullable=False),
    sa.Column('status', sa.Enum('CREATED', 'PENDING', 'PAID', 'SENT', 'RECEIVED', 'CANCELLED', name='orderstatus'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_items',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.BigInteger(), nullable=False),
    sa.Column('order_id', sa.BigInteger(), nullable=False),
    sa.Column('amount', sa.Numeric(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_table('orders')
    op.execute("DROP TYPE orderpaymenttype")
    op.execute("DROP TYPE orderstatus")
    # ### end Alembic commands ###
