# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from app import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8080)  # 监听端口
IOLoop.instance().start()
