#!/usr/bin/env python3

from socket import *
import sys

# 创建udp套接字对象
sockfd = socket(AF_INET, SOCK_DGRAM)


if len(sys.argv) < 3:
    print('''
        argv is error!
        run as
        python3 udp client_udp.py 127.0.0.1 8888
        ''')
    raise
# 读取udp连接参数
IP = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (IP, PORT)

while True:
    # 发送数据
    m = input("请输入：")
    if not m:
        break
    sockfd.sendto(m.encode(), ADDR)

    # 接受数据
    data, addr = sockfd.recvfrom(1024)
    print("服务器%s：%s" % (addr, data.decode()))
