# -*-coding:utf8-*-
__author__ = 'Abbott'

import re
from flask import Blueprint, request, current_app
from sqlalchemy.exc import SQLAlchemyError
from redis.exceptions import RedisError
from app.utils.warpper import success_warp, fail_warp
from app.models.user import check_phone, check_user, add_user, user_login
from app.utils.message import \
    create_verify_code, \
    set_code_in_redis, \
    send_message, \
    get_code_in_redis
from app.utils.token import create_token, set_name_in_redis
from app.utils.md5 import encode_md5

user_page = Blueprint('user', __name__, url_prefix='/user')


@user_page.route('/code', methods=['GET'])
def send_verify_code():
    phone = request.args.get('phone')

    if phone is None or phone == '':
        current_app.logger.error('参数错误')
        return fail_warp('参数错误')

    try:
        if check_phone(phone) is not None:
            current_app.logger.error('{}-电话号码已注册'.format(phone))
            return fail_warp('电话号码已注册')

        code = create_verify_code()
        set_code_in_redis(phone, code)
        send_message(phone, code)

        current_app.logger.info('{}-发送成功'.format(phone))
        return success_warp('发送成功')
    except SQLAlchemyError as e:
        current_app.logger.error('{}-{}-数据库操作失败'.format(e, phone))
        return fail_warp('数据库操作失败')
    except RedisError as e:
        current_app.logger.error('{}-{}-redis操作失败'.format(e, phone))
        return fail_warp('redis操作失败')
    except RuntimeError as e:
        current_app.logger.error('{}-{}-验证码发送失败'.format(e, phone))
        return fail_warp('验证码发送失败')


@user_page.route('/account', methods=['POST'])
def register_account():
    data = request.json
    username = data.get('name')
    password = data.get('password')
    phone = data.get('phone')
    code = data.get('code')

    if phone is None or code is None or username is None or password is None or \
            phone == '' or code == '' or username == '' or password == '':
        current_app.logger.error('{}-参数错误'.format(request.json))
        return fail_warp('参数错误')

    if re.match('^[a-zA-Z][a-zA-Z0-9]{4,15}$', username) is None:
        current_app.logger.error('{}-用户名格式错误'.format(username))
        return fail_warp('用户名格式错误')

    password = encode_md5(password)

    try:
        if check_user(username) is not None:
            current_app.logger.error('{}-用户已存在'.format(username))
            return fail_warp('用户已存在')
        if code == get_code_in_redis(phone):
            add_user(username, password, phone)
            current_app.logger.info('{}-注册成功'.format(username))
            return success_warp('注册成功')
        else:
            current_app.logger.error('{}-验证码错误'.format(username))
            return fail_warp('验证码错误')
    except SQLAlchemyError as e:
        current_app.logger.error('{}-数据库操作失败'.format(e))
        return fail_warp('数据库操作失败')
    except RedisError as e:
        current_app.logger.error('{}-redis操作失败'.format(e))
        return fail_warp('redis操作失败')
    except RuntimeError as e:
        current_app.logger.error('{}-验证码过期'.format(e))
        return fail_warp('验证码过期')


@user_page.route('/authorization', methods=['POST'])
def login():
    data = request.json
    username = data.get('name')
    password = data.get('password')

    if username is None or password is None or \
            username == '' or password == '':
        current_app.logger.error('{}-参数错误'.format(request.json))
        return fail_warp('参数错误')

    password = encode_md5(password)

    try:
        temp = user_login(username, password)
        if temp is not None:
            token = create_token(temp.username)
            set_name_in_redis(temp.username, token)
            current_app.logger.info('{}-登陆成功'.format(request.json))
            return success_warp(str(token, encoding='utf-8'))
        else:
            current_app.logger.error('{}-登陆失败'.format(request.json))
            return fail_warp('登陆失败')
    except SQLAlchemyError as e:
        current_app.logger.error('{}-数据库操作错误'.format(e))
        return fail_warp('数据库操作错误')
    except RedisError as e:
        current_app.logger.error('{}-token保存错误'.format(e))
        return fail_warp('token保存错误')
