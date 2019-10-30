# -*-coding:utf8-*-
__author__ = 'Abbott'

from app.models.models import Notice


def get_notice():
    return Notice.query.order_by(Notice.id.desc()).first()
