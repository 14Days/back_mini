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
    async def get_unknown_img(cls, name: str) -> list:
        user_id = await User.get_user_id(name)
        try:
            async with engine.engine.acquire() as conn:
                res = await conn.execute(cls.user_imgs.select().where(cls.user_imgs.c.user_id == user_id))
                temps = await res.fetchall()
                imgs = []
                from app.models.imgs import Imgs
                for temp in temps:
                    img_url = await Imgs.get_img_url(temp[1])
                    imgs.append({
                        'img_id': temp[1],
                        'img_url': img_url
                    })
                return imgs

        except BaseException as e:
            logger.error(e)
            raise
