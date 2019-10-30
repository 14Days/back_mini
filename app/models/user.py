# -*-coding:utf8-*-
__author__ = 'Abbott'

from app.models.models import User


def check_phone(phone: str):
    return User.query.filter_by(phone=phone).first()
