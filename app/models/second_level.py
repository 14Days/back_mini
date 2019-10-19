import sqlalchemy as sa
from sqlalchemy import ForeignKey

metadata = sa.MetaData()


class SecondLevel():
    second_level = sa.Table(
        'second_level', metadata,
        sa.Column('id', sa.INT, autoincrement=True, primary_key=True),
        sa.Column('top_id', sa.INT, ForeignKey('top_level.id')),
        sa.Column('tag', sa.VARCHAR(255))
    )
