
from socket import *
from time import ctime
#多路复用模块
from select import *
s = socket()
s.bind(('0.0.0.0',8888))
s.listen(5)
inputs = [s]
outputs=[]
while True:
    rs,ws,es = select(inputs,outputs,[])
    for r in rs:
        if r is s:

            connfd,addr=s.accept()
            print('connect from',addr)
            inputs.append(connfd)
        else:

            data = connfd.recv(1024).decode()
            print(data)
            if not data:
                inputs.remove(r)
            outputs.append(r) 
    for w in ws:
        w.send(ctime().encode())
        outputs.remove(w)

            # connfd.send(ctime().encode())



s.close()