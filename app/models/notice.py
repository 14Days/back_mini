import sqlalchemy as sa
from app.models import engine
from aiomysql.sa import Error
import logging

logger = logging.getLogger('main.notice')
metadata = sa.MetaData()


class Notice:
    notice = sa.Table(
        'notice', metadata,
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.VARCHAR(255), nullable=False),
        sa.Column('summary', sa.VARCHAR(1024), nullable=False),
        sa.Column('content', sa.VARCHAR(1024), nullable=True),
        sa.Column('push_day', sa.DateTime, nullable=False)
    )

    @classmethod
    async def get_notice(cls) -> dict:
        try:
            async with engine.engine.acquire() as conn:
                res = await conn.execute(cls.notice.select())
                return await res.fetchone()
        except Error as e:
            logger.error('Failed to select notice from database')
