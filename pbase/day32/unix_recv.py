from socket import *
import sys
#创建流失套接字

#本地套接字不再使用网络地址，而是使用socket类型文件
address='./sockfile'

sockfd=socket(AF_UNIX,SOCK_STREAM)

try :
    sockfd.connect(address)
except error as e:
    print(e)

try:
    message='This is unix message'
    sockfd.send(message.encode())
    data = sockfd.recv(1024).decode()
    print('recv',data)
except error as e:
    print(e)
finally:
    sockfd.close()