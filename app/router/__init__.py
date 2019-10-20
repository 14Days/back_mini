from aiohttp import web
from app.controllers.user import UserHandler
from app.controllers.notice import NoticeHandler
from app.controllers.img import ImgHandler
from app.controllers.tag import TagHandler
from app.middlewares.jwt import jwt_middleware
from app.controllers.record import RecordHandler


def register_routes(app: web.Application):
    user_app = web.Application()
    user = UserHandler()
    user_app.router.add_get('/code', user.send_verify_code)
    user_app.router.add_post('/account', user.register_account)
    user_app.router.add_post('/authorization', user.login)

    notice_app = web.Application()
    notice = NoticeHandler()
    notice_app.middlewares.append(jwt_middleware)
    notice_app.router.add_get('', notice.get_notice)

    img_app = web.Application()
    img = ImgHandler()
    img_app.middlewares.append(jwt_middleware)
    img_app.router.add_get('/cycle', img.get_six_imgs)
    img_app.router.add_get('/imgs', img.get_untabed_imgs)

    tag_app = web.Application()
    tag = TagHandler()
    tag_app.middlewares.append(jwt_middleware)
    tag_app.router.add_post('', tag.post_taged_img)

    record_app = web.Application()
    record = RecordHandler()
    record_app.middlewares.append(jwt_middleware)
    record_app.router.add_get('/day', record.get_work_record)

    app.add_subapp('/user', user_app)
    app.add_subapp('/notice', notice_app)
    app.add_subapp('/img', img_app)
    app.add_subapp('/tag', tag_app)
    app.add_subapp('/record', record_app)
