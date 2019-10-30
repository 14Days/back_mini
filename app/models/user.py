# -*-coding:utf8-*-
__author__ = 'Abbott'

from app.models import db, session_commit
from app.models.models import User


def check_phone(phone: str):
    return User.query.filter_by(phone=phone).first()


def check_user(username: str):
    return User.query.filter_by(username=username).first()


def add_user(username: str, password: str, phone: str):
    user = User(username=username, password=password, open_id=1, phone=phone)
    db.session.add(user)
    session_commit()
