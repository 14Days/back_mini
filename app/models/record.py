# -*-coding:utf8-*-
__author__ = 'Abbott'

import datetime
from datetime import timedelta
from sqlalchemy import and_
from sqlalchemy.sql import func
from app.models import db
from app.models.models import User, Record


def get_record(username: str):
    now = datetime.date.today()
    this_week_start = now - timedelta(days=now.weekday())
    this_week_end = now + timedelta(days=6 - now.weekday())

    user = User.query.filter_by(username=username).first()
    today_record = Record.query.filter_by(user_id=user.id).filter_by(day=now).first()
    if today_record is None:
        temp = Record(day=now, count=0, user_id=user.id)
        db.session.add(temp)
        today_record = Record.query.filter_by(user_id=user.id).filter_by(day=now).first()
    week_record = db.session.query(func.sum(Record.count).label('sums')).select_from(Record). \
        filter(and_(Record.day >= this_week_start, Record.day <= this_week_end, Record.user_id == user.id)).first()

    return today_record.count, week_record.sums
