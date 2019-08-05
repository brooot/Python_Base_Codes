from socket import *
import sys
import os
from time import sleep

class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd

    def do_list(self):
        filelist = os.listdir('.')
        if filelist == None:
            self.connfd.send('FALL'.encode())
        self.connfd.send('OK'.encode())     
        sleep(0.1)
        for filename in filelist:
            if filename[0] != '.' and os.path.isfile(filename):
                self.connfd.send(filename.encode())
            sleep(0.1)
        self.connfd.send('##'.encode())
        print('send file list ok')
        return          

    def do_get(self,filename):
        try:
            fd = open(filename,'rb')
        except:
            self.connfd.send('FALL'.encode())

        self.connfd.send('OK'.encode())    
        sleep(0.1)
        for line in fd:
            self.connfd.send(line)
        fd.close()
        sleep(0.1)
        self.connfd.send('##'.encode())
        print('send file ok')
        return 

        
    def do_put(self):
        pass

def main():
    if len(sys.argv) < 3:
        print('argv is error')
        sys.exit(1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    BUFFERSIZE = 1024
    ADDR = (HOST,PORT)

    #tcp的方式创建套接字
    sockfd = socket()
    sockfd.bind(ADDR)
    sockfd.listen(5)
    while True:
        connfd,addr = sockfd.accept()
        print('Connect from',addr)
        #接收具体需要什么请求
        data = connfd.recv(BUFFERSIZE).decode()
        ftp = FtpServer(connfd)

        if data[0] == 'L':
            ftp.do_list()
        if data[0] == 'G':
            ftp.do_get(data[2:]) 
        if data[0] == 'P':
            ftp.do_put()


if __name__ == '__main__':
    main() 
