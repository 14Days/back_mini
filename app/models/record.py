import sqlalchemy as sa

metadata = sa.MetaData()

record = sa.Table(
    'record', metadata,
    sa.Column('id', sa.INT, autoincrement=True, primary_key=True),
    sa.Column('user_id', sa.INT, ForeignKey='User.id', nullable=False),
    sa.Column('day', sa.DATE, nullable=False),
    sa.Column('count', sa.INT, default=0, nullable=False)
)

