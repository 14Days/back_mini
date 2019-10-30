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


def user_login(username: str, password: str):
    temp_username = User.query.filter_by(username=username).filter_by(password=password).first()
    temp_phone = User.query.filter_by(phone=username).filter_by(password=password).first()
    if temp_username is not None:
        return temp_username
    elif temp_phone is not None:
        return temp_phone
    else:
        return None
