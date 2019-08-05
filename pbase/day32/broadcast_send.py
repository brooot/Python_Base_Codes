from socket import *
import sys
from time import sleep
#设置广播地址<broadcast>是广播地址别名
dest = ('<broadcast>',9999)

s=socket(AF_INET,SOCK_DGRAM)
#设置套接字属性为可发送接受广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
print('press ctrl c to stop')

while True:
    sleep(2)
    s.sendto('村名大家好开会了zhoufa'.encode(),dest)
    data,addr=s.recvfrom(2048)
    print('receive from %s:%s'%(addr,data.decode()))
