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

