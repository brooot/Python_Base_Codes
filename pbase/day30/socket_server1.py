
from socketserver import *
from time import ctime

class Server(ForkingMixIn,TCPServer):
    pass
class Handler(StreamRequestHandler):
    def handler(self):
        #self.request属性即客户端连接后生成的新套接字
        addr = self.request.getpeername()
        print('connect from',addr)

        while True:
            data = self.request.recv(1024).decode()
            print(data)
            if not data:
                break

            self.request.send('[%s]:%s'%(ctime(),data))
server=Server(('0.0.0.0',8889),Handler)
server.serve_forever()
