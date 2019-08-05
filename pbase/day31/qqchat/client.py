from socket import *
from threading import *
HOST = '192.168.75.128'
PORT = 9999  
BUFFERSIZE = 1024
ADDR = (HOST,PORT)
#创建和服务器端同样的套接字类型
sockfd = socket()
#向客户端发起连接请求
sockfd.connect(ADDR)

def send1():
    name=input('输入昵称：')
    sockfd.send(name.encode())
    while True:
        x=input('输入：')
        sockfd.send(x.encode())
def recv1():
    while True:
        # sockfd.send(''.encode())
        data = sockfd.recv(BUFFERSIZE).decode()
        print(data)
if __name__=='__main__':
    t=Thread(target=send1)
    t2=Thread(target=recv1)
    t.start()
    t2.start()
    t.join()
    t2.join()

    sockfd.close()