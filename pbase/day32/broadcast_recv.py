
from socket import *

HOST = ""
PORT = 9999

s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.bind((HOST,PORT))

while True:
    try:
        message,addr=s.recvfrom(2048)
        print('get data from',addr)
        print(message.decode())
        s.sendto('I am coming'.encode(),addr)
    except Exception as e:
        print(e)
