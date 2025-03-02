"""create new tables

Revision ID: c74635cc1194
Revises: a81d9f6ed6d2
Create Date: 2025-03-02 17:17:04.217155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'c74635cc1194'
down_revision: Union[str, None] = 'a81d9f6ed6d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('street', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('house', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('apt', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee_positions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('store_schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day_of_week', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('open_time', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('close_time', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.Column('schedule_id', sa.Integer(), nullable=True),
    sa.Column('scheme', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['schedule_id'], ['store_schedules.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('surname', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('patronymic', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('old', sa.Integer(), nullable=False),
    sa.Column('phone', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('position_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['position_id'], ['employee_positions.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('supplies', sa.Column('store_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'supplies', 'stores', ['store_id'], ['id'], ondelete='RESTRICT')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'supplies', type_='foreignkey')
    op.drop_column('supplies', 'store_id')
    op.drop_table('employees')
    op.drop_table('stores')
    op.drop_table('store_schedules')
    op.drop_table('employee_positions')
    op.drop_table('addresses')
    # ### end Alembic commands ###
