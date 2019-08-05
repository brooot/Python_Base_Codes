
from threading import *
from socket import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)
#线程处理函数，用来处理客户端请求内容
def handler(connfd):
    print('got connection from',connfd.getpeername())
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(data)
        connfd.send('receive your message'.encode())
    connfd.close()


while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(e)
        continue
    t = Thread(target=handler,args=(c,))
    t.setDaemon(True)
    t.start()
s.close()