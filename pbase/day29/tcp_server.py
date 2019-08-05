#!/user/bin/env python3
import socket
from time import ctime
#设置服务器信息
HOST = '127.0.0.1'
PORT = 8888
BUFFERSIZE = 1024

ADDR = (HOST,PORT)

sockfd = socket.socket(socket.AF_INET, 
    socket.SOCK_STREAM)
#绑定服务器IP和PORT
sockfd.bind(ADDR)
#设置监听套接字
sockfd.listen(5)
#准备接收客户端连接
#connfd:新的套接字用来与客户端通信
#addr  所连接的客户端的address

connfd,addr = sockfd.accept()

print('connect from',addr)
while True:

    data = connfd.recv(BUFFERSIZE).decode()

    print('recvive  data:',data)

    connfd.send(('[%s]recv:%s'%(ctime(),data)).encode())

connfd.close()
sockfd.close()
 