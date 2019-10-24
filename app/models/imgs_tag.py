import sqlalchemy as sa
import logging

from sqlalchemy import ForeignKey

from app.models import engine

logger = logging.getLogger('main.imgs_tag')
metadata = sa.MetaData()


class ImgsTag:
    imgs_tag = sa.Table(
        'imgs_tag', metadata,
        sa.Column('img_id', sa.INT, ForeignKey('Imgs.id')),
        sa.Column('tag_id', sa.INT, ForeignKey('SecondLevel.id'))
    )

    @classmethod
    async def add_tag(cls, img_id: int, tag_id: list):
        try:
            async with engine.engine.acquire() as conn:

                task = await conn.begin()
                for tag in tag_id:
                    await conn.execute(cls.imgs_tag.insert().values({
                        "img_id": img_id,
                        "tag_id": tag,
                    }))
                await task.commit()
        except BaseException as e:
            logger.error('Failed to add tag to database')
            raise
