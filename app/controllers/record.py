from .base import Base
from app.models.record import Record
from aiohttp import web


class RecordHandler(Base):
    # 返回打标数
    async def get_work_record(self, request: web.BaseRequest):
        try:
            name = request['name']
            day_count = await Record.get_work_today(name)
            return self.success_warp(day_count)
        except BaseException:
            return self.fail_warp('请求打标数失败')
