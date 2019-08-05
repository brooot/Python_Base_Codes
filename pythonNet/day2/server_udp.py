#!/usr/bin/env python3

from socket import *

# 创建套接字对象
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
IP = '0.0.0.0'
PORT = 8888
ADDR = (IP, PORT)
sockfd.bind(ADDR)

while True:
    # 接受数据(与tcp不同)
    data, addr = sockfd.recvfrom(1024)
    message = "已收到来自%s的数据：%s" % (addr, data.decode())
    print(message)
    # 发送数据
    send_message = "已经收到您的数据。".encode()
    sockfd.sendto(send_message, addr)
sockfd.close()