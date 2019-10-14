import sqlalchemy as sa

metadata = sa.MetaData()


top_level = sa.Table(
    'top_level', metadata,
    sa.Column('id', sa.INT, autoincrement=True, primary_key=True),
    sa.Column('tag', sa.VARCHAR(255))
)