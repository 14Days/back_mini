from aiohttp import web
from app.models.notice import Notice

ping = web.RouteTableDef()


@ping.get('')
async def hello(request: web.BaseRequest):
    notice = Notice()
    res = await notice.select_all()
    data = []
    for item in res:
        temp = dict(item)
        temp['push_day'] = temp['push_day'].strftime('%Y-%m-%d')
        data.append(temp)

    return web.json_response({
        'status': 'success',
        'data': data
    })
