# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Blueprint, g
from app.utils.warpper import success_warp

record_page = Blueprint('record', __name__, url_prefix='/record')


@record_page.route('', methods=['GET'])
def get_count():
    return success_warp(g.username)
