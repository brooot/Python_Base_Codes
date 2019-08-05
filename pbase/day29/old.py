from socket import *
import sys
class FtpClient(object):
    def __init__(self,serveraddr):
        self.serveraddr=serveraddr
    def do_list(self):
        sockfd=socket()
        sockfd.connect(self.ser)
def main():
    if len(sys.argv)<3:
        print('argv is error')
    host=sys.argv[1]
    port=int(sys.argv[2])
    BUFFERSIZE=1024
    addr=(host,port)

    # sockfd=socket()
while True:
    print('**command    **')
    print('**list       **')
    print('**get        **')
    print('**put filename**')
    print('**quit       **')
    data=input('shuru')
    ftp=FtpClient(addr)
    if data[:4]=='list':
        ftp.do_list()
    elif data[:3]=='get':

        ftp.do_get()
    elif data=='put':
        pass
    else:
        sys.quit(0)



if __name__=='__main__':
    main()
