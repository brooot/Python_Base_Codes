from socket import * 
from threading import Thread
import pymysql
import re

s=socket()
s.bind(('192.168.75.128',9999))
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.listen(5)
l = []
def handler(x):
    
    print('connect from',x.getpeername())
    info=x.recv(1024).decode()
    if info='login':
        pass
    elif info='register':
        pass
           
    while True:




    l.remove(x)
    t.join()
    connfd.close()
def server_send():
    while True:
        g=input('server输入：')
        for i in l:
            i.send('server say: %s'%g.encode())

        
while True:
    try:
        connfd,addr=s.accept()
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(e)
        continue
    # l.append(connfd)
    t = Thread(target=handler,args=(connfd,))
    t.start()

s.close()