import sqlalchemy as sa
import logging
from app.models import engine
from app.models.user import User

metadata = sa.MetaData()
logger = logging.getLogger('models.user_imgs')


class UserImgs:
    user_imgs = sa.Table(
        'user_imgs', metadata,
        sa.Column('user_id', sa.Integer, sa.ForeignKey('User.id')),
        sa.Column('img_id', sa.Integer, sa.ForeignKey('Imgs.id'))
    )

    @classmethod
    async def add_unknown_img(cls, name: str, img_id: int):
        user_id = await User.get_user_id(name)
        try:
            async with engine.engine.acquire() as conn:
                task = await conn.begin()
                print(cls.user_imgs.insert().values({
                    'img_id': img_id,
                    'user_id': user_id
                }))

                await conn.execute(cls.user_imgs.insert().values({
                    'img_id': img_id,
                    'user_id': user_id
                }))
                await task.commit()
        except BaseException as e:
            logger.error('Failed to add unknown img to database')
            raise
