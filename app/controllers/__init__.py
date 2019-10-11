from aiohttp import web


async def hello(request: web.BaseRequest):
    return web.json_response({
        'status': 'success'
    })
