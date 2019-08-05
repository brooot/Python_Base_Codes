from socket import *

from time import sleep, ctime

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 8888))
s.listen(3)

# 将套接字设置超时间
s.settimeout(5)

while True:
    print("waiting for connection...")
    try:
        c, addr = s.accept()
    except timeout:  # timeout
        print(ctime())
        continue
    else:
        print("connect from :", addr)
        while True:
            data = c.recv(1024).decode()
            if not data:
                break
            print(data)
            c.send(ctime().encode())
        c.close()
    s.close()
