from .base import Base
from aiohttp import web
from app.models.imgs import Imgs
from app.models.user_imgs import UserImgs


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
            data = []
            for item in res:
                data.append({
                    'img_id': item[0],
                    'img_url': item[1]
                })

            if data is None:
                return self.fail_warp('请求图片失败')
            return self.success_warp(data)
        except BaseException as e:
            return self.fail_warp("请求图片失败")

    # 提交搁置图片
    async def post_unknown_imgs(self, request: web.BaseRequest):
        try:
            data = await request.json()
            img_id = data['img_id']
            name = request['name']
            await Imgs.change_iskonwn(img_id, name)
            return self.success_warp('请求成功')
        except BaseException:
            return self.fail_warp('添加搁置图片失败')

    # 请求搁置图片
    async def get_unknown_imgs(self, request: web.BaseRequest):
        try:
            name = request['name']
            res = await UserImgs.get_unknown_img(name)
            return self.success_warp(res)
        except BaseException:
            return self.fail_warp('请求搁置图片失败')

