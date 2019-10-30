# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from redis.exceptions import RedisError
from requests.exceptions import RequestException
from app.utils.warpper import success_warp, fail_warp
from app.models.user import check_phone, check_user, add_user
from app.utils.message import \
    create_verify_code, \
    set_code_in_redis, \
    send_message, \
    get_code_in_redis

user_page = Blueprint('user', __name__, url_prefix='/user')


@user_page.route('/code', methods=['GET'])
def send_verify_code():
    phone = request.args.get('phone')

    if phone is None or phone == '':
        return fail_warp('参数错误')

    try:
        if check_phone(phone) is not None:
            return fail_warp('电话号码已注册')
        code = create_verify_code()
        set_code_in_redis(phone, code)
        send_message(phone, code)
        return success_warp('发送成功')
    except SQLAlchemyError as e:
        return fail_warp('数据库操作失败')
    except RedisError as e:
        return fail_warp('redis操作失败')
    except RequestException as e:
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
        return fail_warp('参数错误')

    try:
        if check_user(username) is not None:
            return fail_warp('用户已存在')
        if code == get_code_in_redis(phone):
            add_user(username, password, phone)
            return success_warp('注册成功')
        else:
            return fail_warp('验证码错误')
    except SQLAlchemyError as e:
        return fail_warp('数据库操作失败')
    except RedisError as e:
        return fail_warp('redis操作失败')
    except RuntimeError as e:
        return fail_warp('验证码过期')
