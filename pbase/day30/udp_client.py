from socket import *
from threading import *
from time import sleep
host = '0.0.0.0'
post = 6666
BUFFERSIZE = 1024
addr = (host, post)

sockfd = socket(AF_INET, SOCK_DGRAM)


# def f1(fd):

#     while True:
#         data,address = fd.recvfrom(BUFFERSIZE)
#         print(data.decode())


def f2():
    # fd.sendto('nihao'.encode(),addr)

    while True:
        x=input('shui:')
        sockfd.sendto('1234'.encode(),addr)



t = Thread(target=f2,)

# t2 = Thread(target=f1, args=(sockfd,))
t.start()
sleep(1)
# t2.start()


# while True:
#     data = input('your message>>')
#     if not data:
#         break
#     sockfd.sendto(data.encode(),addr)
#     data,addr = sockfd.recvfrom(BUFFERSIZE)
#     print(data.decode())

sockfd.close()
