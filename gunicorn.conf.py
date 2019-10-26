# 定义同时开启的处理请求的进程数量，根据网站流量适当调整
workers = 1
worker_class = 'aiohttp.GunicornWebWorker'
bind = '0.0.0.0:8080'
