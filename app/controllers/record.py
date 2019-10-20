from .base import Base
from app.models.record import Record
from aiohttp import web


class RecordHandler(Base):
    # 返回每日打标数
    async def get_work_today(self, request: web.BaseRequest):
        try:
            name = request['name']
            day_count = await Record.get_work_today(name)
            return self.success_warp(day_count)
        except BaseException:
            return self.fail_warp('请求日打标数失败')
