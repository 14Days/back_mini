from .base import Base
from aiohttp import web
from models.imgs import Imgs


class ImgHandler(Base):
    # 请求轮播图
    async def get_six_imgs(self, request: web.BaseRequest):
        try:
            lists = await Imgs.return_six_images()
            data = []

            for item in lists:
                temp = dict(item).get('img_url')
                if temp is not None:
                    data.append(temp)

            if data is None:
                return self.fail_warp('请求轮播图失败')
            return self.success_warp(data)
        except BaseException as e:
            return self.fail_warp('请求轮播图失败')

    # 请求未被打标的图片
    async def get_untabed_imgs(self, request: web.BaseRequest):
        try:
            num = request.query.get('num')
            res = await Imgs.return_untaged_imgs(int(num))
            print(res)
            data = {}
            for item in res:
                data[item[0]] = item[1]

            if data is None:
                return self.fail_warp('请求图片失败')
            return self.success_warp(data)
        except BaseException as e:
            return self.fail_warp("请求图片失败")


