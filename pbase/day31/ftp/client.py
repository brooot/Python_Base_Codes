from socket import * 
import sys 

class FtpClient(object):
    def __init__(self,serveraddr):
        self.serveraddr = serveraddr

    def do_list(self):
        sockfd = socket()
        sockfd.connect(self.serveraddr)
        sockfd.send('L'.encode())

        data = sockfd.recv(1024).decode()
        if data == 'OK':
            while True:
                data = sockfd.recv(1024).decode()
                if data == '##':
                    break
                print(data)
            print('List OK!')
            sockfd.close()
            return
        else:
            print('List error!')
            sockfd.close()
            return

    def do_get(self,filename):
        fd = open(filename,'w')
        data = 'G ' + filename
        sockfd = socket()
        sockfd.connect(self.serveraddr)
        sockfd.send(data.encode())

        data = sockfd.recv(1024).decode()
        if data == 'OK':
            while True:
                data = sockfd.recv(1024).decode()
                if data == '##':
                    break
                print(data)
                fd.write(data)
            fd.close()
            print('get file OK!')
            sockfd.close()
            return
        else:
            print('get file error!')
            sockfd.close()
            return

    def do_put(self,filename):
        pass


def main():
    if len(sys.argv) < 3:
        print('argv is error')
        sys.exit(1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    BUFFERSIZE = 1024
    ADDR = (HOST,PORT)

    while True:
        print('*******command*********')
        print('*******  list  ********')
        print('******get filename*****')
        print('******put filename*****')
        print('*******  quit  ********') 
        data = input('Input command>>')

        ftp = FtpClient(ADDR)

        if data[:4] == 'list':
            ftp.do_list()
        elif data[:3] == 'get':
            filename = data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[:3] == 'put':
            filename = data.split(' ')[-1]
            ftp.do_put(filename) 
        elif data == 'quit':
            sys.exit(0)
        else:
            continue



if __name__ == '__main__':
    main()