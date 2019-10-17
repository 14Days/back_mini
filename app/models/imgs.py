import sqlalchemy as sa
import logging
from app.models import engine
from aiomysql.sa import Error

logger = logging.getLogger('main.imgs')
metadata = sa.MetaData()


class Imgs:
    imgs = sa.Table(
        'imgs', metadata,
        sa.Column('id', sa.INT, autoincrement=True, primary_key=True),
        sa.Column('img_url', sa.VARCHAR(255)),
        sa.Column('is_tabed', sa.Boolean, default=False)
    )

    @classmethod
    async def return_six_images(cls) -> list:
        try:
            async with engine.engine.acquire() as conn:
                res = await conn.execute(Imgs.imgs.select())
                return await res.fetchmany(6)
        except Error as e:
            logger.error('Failed to select six imges from database')

    @classmethod
    async def return_untabed_imgs(cls, num: int) -> list:
        try:
            async with engine.engine.acquire() as conn:
                res = await conn.execute(cls.imgs.select().where(cls.imgs.c.is_tabed == False))
                return await res.fetchmany(num)
        except Error as e:
            logger.error('Failed to select imgs from database')
