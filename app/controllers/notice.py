# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Blueprint
from sqlalchemy.exc import SQLAlchemyError
from app.utils.warpper import fail_warp, success_warp
from app.models.notice import get_notice

notice_page = Blueprint('notice', __name__, url_prefix='/notice')


@notice_page.route('', methods=['GET'])
def notice():
    try:
        temp = get_notice()
        if temp is None:
            return fail_warp('没有通知')
        else:
            return success_warp({
                'title': temp.title,
                'content': temp.content
            })
    except SQLAlchemyError:
        return fail_warp('数据库操作错误')
