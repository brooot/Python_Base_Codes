from socket import *
HOST = '0.0.0.0'
PORT = 8888
BUFFERSIZE = 1024
ADDR = (HOST,PORT)
#创建和服务器端同样的套接字类型
sockfd = socket()
#向客户端发起连接请求
sockfd.connect(ADDR)
while True:
    data = input('>>')
    if not data:
        sockfd.send(''.encode())
        break
    sockfd.send(data.encode())
    data = sockfd.recv(BUFFERSIZE).decode()
    print(data)
print(data)
sockfd.close()