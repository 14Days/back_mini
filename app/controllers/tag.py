# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Blueprint, request, g
from sqlalchemy.exc import SQLAlchemyError
from app.utils.warpper import success_warp, fail_warp
from app.models.tag import tag_it, unknown_img

tag_page = Blueprint('tag', __name__, url_prefix='/tag')


@tag_page.route('', methods=['POST'])
def tag_img():
    username = g.username
    data = request.json
    img_id = data.get('img_id')
    tag = data.get('tag')

    if img_id is None or tag is None or \
            img_id == '':
        return fail_warp('参数错误')

    try:
        tag_it(img_id, tag, username)
        return success_warp('打标成功')
    except SQLAlchemyError:
        return fail_warp('数据库操作错误')


@tag_page.route('/unknown', methods=['GET'])
def set_unknown_img():
    img_id = request.args.get('img_id')

    if img_id is None:
        return fail_warp('参数错误')

    try:
        unknown_img(img_id)
        return success_warp('搁置成功')
    except SQLAlchemyError:
        return fail_warp('数据库操作错误')
