# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Blueprint, request, g
from sqlalchemy.exc import SQLAlchemyError
from app.utils.warpper import success_warp, fail_warp
from app.models.img import get_swiper_item, get_tag_item, untag_img, get_unknown_img

img_page = Blueprint('img', __name__, url_prefix='/img')


@img_page.route('/cycle', methods=['GET'])
def get_swiper():
    try:
        images = get_swiper_item()
        data = []
        for image in images:
            data.append(image.img_url)

        return success_warp(data)
    except SQLAlchemyError:
        return fail_warp('数据库操作失败')


@img_page.route('/tags', methods=['GET'])
def get_tags():
    try:
        all_tags = get_tag_item()
        data = []
        for first in all_tags:
            second_tags = []
            for second in first.second_tag:
                second_tags.append({
                    'id': second.id,
                    'tag': second.tag
                })
            data.append({
                'top': first.tag,
                'second': second_tags
            })

        return success_warp(data)
    except SQLAlchemyError:
        return fail_warp('数据库操作失败')


@img_page.route('/imgs', methods=['GET'])
def get_untabed_imgs():
    num = request.args.get('num')
    if num is None:
        return fail_warp('参数错误')
    username = g.username
    try:
        images = untag_img(num, username)
        data = []
        for image in images:
            data.append({
                'id': image.id,
                'url': image.img_url
            })
        return success_warp(data)
    except SQLAlchemyError:
        return fail_warp('数据库操作错误')


@img_page.route('/unknown', methods=['GET'])
def get_unknown():
    username = g.username
    try:
        images = get_unknown_img(username)
        data = []
        for image in images:
            data.append({
                'id': image.id,
                'url': image.img_url
            })
        return success_warp(data)
    except SQLAlchemyError:
        return fail_warp('数据库操作错误')
