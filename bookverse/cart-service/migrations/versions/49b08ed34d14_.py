"""empty message

Revision ID: 49b08ed34d14
Revises: 
Create Date: 2023-08-29 01:34:32.397672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49b08ed34d14'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ebook',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('pages', sa.Integer(), nullable=True),
    sa.Column('authors', sa.String(length=255), nullable=True),
    sa.Column('year_of_release', sa.Integer(), nullable=True),
    sa.Column('file_path', sa.String(length=255), nullable=True),
    sa.Column('cover_path', sa.String(length=255), nullable=True),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.Column('price_cents', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ebook_cart',
    sa.Column('ebook_id', sa.Integer(), nullable=True),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.ForeignKeyConstraint(['ebook_id'], ['ebook.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ebook_cart')
    op.drop_table('ebook')
    op.drop_table('cart')
    # ### end Alembic commands ###