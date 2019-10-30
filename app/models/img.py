# -*-coding:utf8-*-
__author__ = 'Abbott'

from sqlalchemy import or_, and_
from app.models import session_commit
from app.models.models import User, Img, TopLevel, SecondLevel


def get_swiper_item():
    return Img.query.limit(5).all()


def get_tag_item():
    return TopLevel.query.join(SecondLevel).all()


def untag_img(num: int, username: str):
    user = User.query.filter_by(username=username).first()
    images = Img.query. \
        filter(or_(and_(Img.user_id.isnot(None), Img.status == 0), Img.user_id.is_(None))).limit(num).all()

    for image in images:
        image.user_id = user.id
    session_commit()

    return images


def get_unknown_img(username):
    user = User.query.filter_by(username=username).first()
    return Img.query.filter_by(user_id=user.id).filter_by(status=2).all()
