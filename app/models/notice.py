import sqlalchemy as sa

metadata = sa.MetaData()

notice = sa.Table(
    'notice', metadata,
    sa.Column('id', sa.INT, primary_key=True, autoincrement=True),
    sa.Column('title', sa.VARCHAR(255), nullable=False),
    sa.Column('summary', sa.VARCHAR(1024), nullable=False),
    sa.Column('content', sa.VARCHAR(1024), nullable=True),
    sa.Column('push_day', sa.DATETIME, nullable=False)
)


