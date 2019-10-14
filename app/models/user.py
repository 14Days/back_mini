import sqlalchemy as sa

metadata = sa.MetaData()


user = sa.Table(
    'user', metadata,
    sa.Column('id', sa.INT, primary_key=True, autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(50)),
    sa.Column('password', sa.VARCHAR(255)),
    sa.Column('open_id', sa.VARCHAR(255)),
    sa.Column('phone', sa.CHAR(11))
)
