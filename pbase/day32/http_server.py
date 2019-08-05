#coding=utf-8
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    #当获取到get请求就用do_GET方法处理
    def do_GET(self):
        print('do method get')
        #获取客户端的请求内容
        print(self.rfile.read(128))
        #获取客户端发送响应的内容
        print(self.wfile.write('hello httpserver'))
        return
    def do_POST(self):
        return

address = ('127.0.0.1',8000)
#创建server对象，第二个参数为处理请求类名    
server = HTTPServer(address,RequestHandler)
#启动http服务器
server.serve_forever()