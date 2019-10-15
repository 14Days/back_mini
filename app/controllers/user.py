from aiohttp import web
from .base import Base
from app.utils.message import create_verify_code, set_code_in_redis, send_message, get_code_in_redis
from app.models.user import User


# 注册接口
class UserHandler(Base):
    async def send_verify_code(self, request: web.BaseRequest):
        phone_number = request.query.get('phone')

        if phone_number is None:
            return self.fail_warp('电话号码不能为空')

        if not await User.check_phone(phone_number):
            return self.fail_warp('已存在电话号码')

        code = create_verify_code()
        await set_code_in_redis(phone_number, code)
        result = await send_message(phone_number, code)
        if not result:
            return self.fail_warp('短信发送失败')
        return self.success_warp('短信发送成功')

    async def register_account(self, request: web.BaseRequest):
        data = await request.json()

        if data.get('phone') is None or data.get('code') is None:
            return self.fail_warp('缺少参数')

        if data.get('code') == await get_code_in_redis(data.get('phone')):
            await User.add_user(data.get('username'), data.get('password'), data.get('phone'))
            return self.success_warp('验证成功')
        else:
            return self.fail_warp('验证码错误')
