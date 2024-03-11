"""New revision

Revision ID: f857f4ff25e1
Revises: f656c035f9f2
Create Date: 2024-03-11 11:41:52.177449

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f857f4ff25e1'
down_revision: Union[str, None] = 'f656c035f9f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teams_id', sa.Integer(), nullable=True),
    sa.Column('started_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('ended_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tournament',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('is_ended', sa.Boolean(), nullable=True),
    sa.Column('type', sa.Enum('all_vs_all', 'play_off', 'groups', name='tournament_type'), nullable=True),
    sa.Column('started_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('ended_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Tournament')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Tournament',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Tournament_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_ended', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('started_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('ended_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Tournament_pkey')
    )
    op.drop_table('tournament')
    op.drop_table('team')
    op.drop_table('game')
    # ### end Alembic commands ###