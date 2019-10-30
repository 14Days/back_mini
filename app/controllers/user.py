# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')
