from .base import Base
from aiohttp import web
from app.models.notice import Notice


class NoticeHandler(Base):
    # 请求通知接口
    async def get_notice(self, request: web.BaseRequest):
        notice = await Notice.get_notice()
        if notice is None:
            return self.fail_warp('请求公告失败')
        return self.success_warp(notice[3])
