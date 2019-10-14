from aiohttp import web
from .base import Base
from app.models.notice import Notice


class Ping(Base):
    async def hello(self, request: web.BaseRequest):
        notice = Notice()
        res = await notice.select_all()
        data = []
        for item in res:
            temp = dict(item)
            temp['push_day'] = temp['push_day'].strftime('%Y-%m-%d')
            data.append(temp)

        return self.success_warp(data)
