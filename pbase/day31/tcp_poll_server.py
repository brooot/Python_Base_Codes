from socket import *
from time import ctime
#多路复用模块
from select import *

s = socket()
s.bind(('0.0.0.0',9999))
s.listen(5)
fdmap={s.fileno():s}
#创建poll对象
p=poll()
#注册关注对象
p.register(s)

while True:
    #等待任意一个注册事件返回
    #[(fileno,ioobj),(),()]
    events=p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = s.accept()
            print('connect from',addr)
            p.register(s)
            fdmap[c.fileno()]=c

        elif event & POLLIN:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unreg ister(fd)
                del fdmap[fd]
            print(data)
            fdmap[fd].send('receive your message'.encode())
s.close()
