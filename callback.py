import os
import tornado.web
import tornado.ioloop
import logging
import requests
import json

class CallBackHandler(tornado.web.RequestHandler):
    def post(self, *args, **argd):
        self.clear()
        self.set_status(200)
        print(self.request)
        print(self.request.headers)
        print(self.request.body)
        self.write('success')

app = tornado.web.Application([
    (r'/callback', CallBackHandler)
    ])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()
