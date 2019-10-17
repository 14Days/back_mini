from aiohttp import web
from app.controllers.ping import Ping
from app.controllers.user import UserHandler
from app.controllers.notice import NoticeHandler
from app.controllers.img import ImgHandler


def register_routes(app: web.Application):
    ping_app = web.Application()
    ping = Ping()
    ping_app.router.add_get('', ping.hello)

    user_app = web.Application()
    user = UserHandler()
    user_app.router.add_get('/code', user.send_verify_code)
    user_app.router.add_post('/account', user.register_account)
    user_app.router.add_post('/authorization', user.login)

    notice_app = web.Application()
    notice = NoticeHandler()
    notice_app.router.add_get('', notice.get_notice)

    img_app = web.Application()
    img = ImgHandler()
    img_app.router.add_get('/cycle', img.get_six_imgs)
    img_app.router.add_get('/imgs', img.get_untabed_imgs)

    app.add_subapp('/ping', ping_app)
    app.add_subapp('/user', user_app)
    app.add_subapp('/notice', notice_app)
    app.add_subapp('/img', img_app)
