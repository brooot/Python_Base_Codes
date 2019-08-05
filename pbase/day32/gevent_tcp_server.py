import gevent
from gevent import monkey
monkey.patch_all()
from socket import *
from time import ctime
import sys

#接受客户端连接，每接收一个客户端请求就注册一个协程事件
def server(addr):
    s=socket()
    s.bind(addr)
    s.listen(5)
    while True:
        c,client_addr=s.accept()
        gevent.spawn(handler,c,client_addr)


#处理和客户端的通信
def handler(c,addr):
    print('connect from',addr)
    try:
        while True:
            data = c.recv(1024).decode()
            if not data:
                break
            print(data)
            c.send(ctime().encode())
    except Exception as e:
        print(e)
    finally:
        c.close()

if __name__=='__main__':
    if len(sys.argv)<3:
        print('argv error')
        sys.exit(1)
    host=sys.argv[1]
    port=int(sys.argv[2])
    addr=(host,port)
    server(addr)
