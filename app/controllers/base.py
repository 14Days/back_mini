from aiohttp import web


class Base:
    @staticmethod
    def success_warp(data):
        return web.json_response({
            'status': 'success',
            'data': data
        })

    @staticmethod
    def fail_warp(msg):
        return web.json_response({
            'status': 'error',
            'err_msg': msg
        })
