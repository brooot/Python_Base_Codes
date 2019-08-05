from socket import *
from threading import *
import sys

l=[]

while True:
    print('waiting for message...')
    # 得到客户端信息和地址
    data, addr = sockfd.recvfrom(1024)
    if addr not in l:
        l.append(addr)
    print('recv from', addr, data)

    sockfd.sendto(data, addr)
sockfd.close()



if __name__=='__main__':
    if len(sys.argv)<3:
        print('argv error')
        sys.exit(1)
    host=sys.argv[1]
    port=int(sys.argv[2])
    sockfd = socket(AF_INET, SOCK_DGRAM)
    sockfd.bind(addr)

