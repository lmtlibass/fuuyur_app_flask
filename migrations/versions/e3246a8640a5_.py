"""empty message

Revision ID: e3246a8640a5
Revises: 
Create Date: 2022-08-16 02:49:52.573172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3246a8640a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('venu_id', sa.Integer(), nullable=True))
    op.add_column('shows', sa.Column('artist_id', sa.Integer(), nullable=True))
    op.drop_constraint('shows_venu_fkey', 'shows', type_='foreignkey')
    op.drop_constraint('shows_artist_fkey', 'shows', type_='foreignkey')
    op.create_foreign_key(None, 'shows', 'artists', ['artist_id'], ['id'])
    op.create_foreign_key(None, 'shows', 'venues', ['venu_id'], ['id'])
    op.drop_column('shows', 'artist')
    op.drop_column('shows', 'venu')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('venu', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('shows', sa.Column('artist', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.create_foreign_key('shows_artist_fkey', 'shows', 'artists', ['artist'], ['id'])
    op.create_foreign_key('shows_venu_fkey', 'shows', 'venues', ['venu'], ['id'])
    op.drop_column('shows', 'artist_id')
    op.drop_column('shows', 'venu_id')
    # ### end Alembic commands ###