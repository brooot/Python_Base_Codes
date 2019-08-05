from socket import *
import sys
class FtpServer(object):
    pass

def main():
    if len(sys.argv)<3:
        print('argv is error')
    host=sys.argv[1]
    port=int(sys.argv[2])
    BUFFERSIZE=1024
    addr=(host,port)

    sockfd=socket()
    sockfd.bind(addr)
    sockfd.listen(5)
    while True:
        connfd,addr=sockfd.accept()
        print('connect from',addr)
        #接收具体需要什么请求
        data=connfd.recv(BUFFERSIZE)
        if data=='list':
            pass
        elif data=='get':
            pass
        elif data=='put':
            pass


if __name__=='__main__':
    main()
