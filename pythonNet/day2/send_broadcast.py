from socket import *
from time import sleep

# 设置目标地址
dest = ("192.168.136.255", 9870)

s = socket(AF_INET, SOCK_DGRAM)

# 设置能够发送广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    sleep(2)
    s.sendto("这是广播。".encode(), dest)
s.close()