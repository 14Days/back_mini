# -*-coding:utf8-*-
__author__ = 'Abbott'

import datetime
from app.models import session_commit, db
from app.models.models import User, Img, img_tag, Record


def tag_it(img_id: int, tag: list, username: str):
    # 图片打标
    for item in tag:
        img_tag.insert().values({
            "img_id": img_id,
            "tag_id": item,
        })

    # 图片标记为已操作
    image = Img.query.filter_by(id=img_id).first()
    image.status = 1

    # 用户记录加一
    user = User.query.filter_by(username=username).first()
    record = Record.query.filter_by(user_id=user.id).filter_by(day=datetime.date.today()).first()
    if record is None:
        temp = Record(day=datetime.date.today(), count=1, user_id=user.id)
        db.session.add(temp)
    else:
        record.count = record.count + 1
    session_commit()
