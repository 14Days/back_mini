from aiohttp import web
from .base import Base
from app.models.imgs import Imgs
from app.models.imgs_tag import ImgsTag


class TagHandler(Base):
    # 提交已经打标完成的图片
    async def post_taged_img(self, request: web.BaseRequest):
        data = await request.json()
        name = request['name']

        if data is None:
            return self.fail_warp('参数不能为空')
        img_id = data.get('img_id')
        tag_id = data.get('tag')

        try:
            # 标记img表中对应图片为已打标
            await Imgs.change_istaged(img_id)
            # 为提交的图片添加标签
            await ImgsTag.add_tag(img_id, tag_id)
            # 用户日打标数加一，周打标数加一

            return self.success_warp('图片提交完成')
        except BaseException:
            return self.fail_warp('提交失败')
