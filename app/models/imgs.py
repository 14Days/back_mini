import sqlalchemy as sa

metadata = sa.MetaData()

imgs = sa.Table(
    'imgs', metadata,
    sa.Column('id', sa.INT, autoincrement=True, primary_key=True),
    sa.Column('img_url', sa.VARCHAR(255))
)
