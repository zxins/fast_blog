"""update models

Revision ID: 1db4146e6ad4
Revises: e8f6bf13cb07
Create Date: 2021-01-13 09:08:00.357537

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1db4146e6ad4'
down_revision = 'e8f6bf13cb07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('book_catalogs_ibfk_1', 'book_catalogs', type_='foreignkey')
    op.drop_column('book_catalogs', 'book_id')
    op.drop_constraint('book_images_ibfk_1', 'book_images', type_='foreignkey')
    op.drop_column('book_images', 'book_id')
    op.drop_constraint('books_ibfk_1', 'books', type_='foreignkey')
    op.drop_column('books', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False, comment='关联用户id'))
    op.create_foreign_key('books_ibfk_1', 'books', 'users', ['user_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('book_images', sa.Column('book_id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('book_images_ibfk_1', 'book_images', 'books', ['book_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('book_catalogs', sa.Column('book_id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('book_catalogs_ibfk_1', 'book_catalogs', 'books', ['book_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###