import sqlalchemy as sa
from aiomysql.sa import connection

metadata = sa.MetaData()
conn = connection()

notice = sa.Table(
    'notice', metadata,
    sa.Column('id', sa.INT, primary_key=True, autoincrement=True),
    sa.Column('title', sa.VARCHAR(255), nullable=False),
    sa.Column('summary', sa.VARCHAR(1024), nullable=False),
    sa.Column('content', sa.VARCHAR(1024), nullable=True),
    sa.Column('push_day', sa.DATETIME, nullable=False)
)


async def return_notice():
    sql = notice.select()

