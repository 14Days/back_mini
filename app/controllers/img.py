from .base import Base
from aiohttp import web
from models.imgs import Imgs


class ImgHandler(Base):
    # 请求轮播图
    async def get_six_imgs(self, request: web.BaseRequest):
        lists = await Imgs.return_six_images()
        data = []

        for item in lists:
            temp = dict(item).get('img_url')
            if temp is not None:
                data.append(temp)

        if data is None:
            return self.fail_warp('请求轮播图失败')
        return self.success_warp(data)

    # 请求未被打标的图片
    async def get_untabed_imgs(self, request: web.BaseRequest):
        num = request.query.get('num')
        res = await Imgs.return_untabed_imgs(int(num))
        data = []
        for item in res:
            data.append(item[1])

        if data is None:
            return self.fail_warp('请求图片失败')
        return self.success_warp(data)

    #提交已经打标完成的图片
    async def post_tabed_img(self, request:web.BaseRequest):
        url = request.query.get('url')
        #标记img表中对应图片为已打标

        #

