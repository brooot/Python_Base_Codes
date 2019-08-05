from socket import *
from time import ctime

host = '0.0.0.0'
post = 6666
BUFFERSIZE = 1024
addr = (host, post)
# 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.bind(addr)

while True:
    print('waiting for message...')
    # 得到客户端信息和地址
    data, addr = sockfd.recvfrom(BUFFERSIZE)
    print('recv from', addr, data)
    s = input('shuru:')
    # 向客户端发送消息指明发送给谁
    sockfd.sendto(s.encode(), addr)
sockfd.close()
