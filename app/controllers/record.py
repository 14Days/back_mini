# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Blueprint, g
from sqlalchemy.exc import SQLAlchemyError
from app.utils.warpper import success_warp, fail_warp
from app.models.record import get_record

record_page = Blueprint('record', __name__, url_prefix='/record')


@record_page.route('', methods=['GET'])
def get_count():
    username = g.username
    try:
        today, week_record = get_record(username)
        return success_warp({
            'day': today,
            'week': int(week_record)
        })
    except SQLAlchemyError:
        return fail_warp('数据库操作失败')
