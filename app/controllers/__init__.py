# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Flask
from app.controllers.user import user_page


def register_routers(app: Flask):
    app.register_blueprint(user_page)
