from aiohttp import web


ping = web.RouteTableDef()


@ping.get('')
async def hello(request: web.BaseRequest):
    return web.json_response({
        'status': 'success'
    })
