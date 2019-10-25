import sqlalchemy as sa
import logging
import datetime
from app.models import engine
from app.models.imgs_tag import ImgsTag
from app.models.user import User
from app.models.record import Record
from aiomysql.sa import Error

logger = logging.getLogger('main.imgs')
metadata = sa.MetaData()


class Imgs:
    imgs = sa.Table(
        'imgs', metadata,
        sa.Column('id', sa.INT, autoincrement=True, primary_key=True),
        sa.Column('img_url', sa.VARCHAR(255)),
        sa.Column('is_tabed', sa.Integer, default=False)
    )

    @classmethod
    async def return_six_images(cls) -> list:
        try:
            async with engine.engine.acquire() as conn:
                res = await conn.execute(Imgs.imgs.select())
                return await res.fetchmany(6)
        except Error as e:
            logger.error('Failed to select six imges from database', e)
            raise

    @classmethod
    async def return_untaged_imgs(cls, num: int) -> list:
        try:
            async with engine.engine.acquire() as conn:
                res = await conn.execute(cls.imgs.select().where(cls.imgs.c.is_tabed == 0))
                return await res.fetchmany(num)
        except Error as e:
            logger.error('Failed to select imgs from database', e)
            raise

    @classmethod
    async def change_istaged(cls, img_id: int, tag_id: list, name: str):
        try:
            async with engine.engine.acquire() as conn:
                task = await conn.begin()
                await conn.execute(cls.imgs.update().where(cls.imgs.c.id == img_id).values(is_tabed=1))

                for tag in tag_id:
                    await conn.execute(ImgsTag.imgs_tag.insert().values({
                        "img_id": img_id,
                        "tag_id": tag,
                    }))

                date = datetime.date.today()
                user_id = await User.get_user_id(name)

                res = await conn.execute(
                    Record.record.select().where(Record.record.c.day == date).where(Record.record.c.user_id == user_id))
                temp = await res.fetchone()

                if temp is None:
                    await conn.execute(Record.record.insert().values(user_id=user_id, day=date, count=1))
                else:
                    count = temp[3] + 1
                    await conn.execute(Record.record.update().where(Record.record.c.user_id == user_id).where(
                        Record.record.c.day == date).values(count=count))
                await task.commit()

        except Error as e:
            logger.error('Failed to change tag in database', e)
            raise

    @classmethod
    async def change_iskonwn(cls, img_id: int):
        try:
            async with engine.engine.acquire() as conn:
                task = await conn.begin()
                await conn.execute(cls.imgs.update().where(cls.imgs.c.id == img_id).values(is_tabed=2))
                await task.commit()
        except Error as e:
            logger.error('Failed to change isknown in database', e)
            raise

    @classmethod
    async def get_img_url(cls, img_id: int) -> str:
        try:
            async with engine.engine.acquire() as conn:
                res = await conn.execute(cls.imgs.select().where(cls.imgs.c.id == img_id))
                temp = await res.fetchone()
                return temp[1]
        except Error as e:
            logger.error(e)
            raise
