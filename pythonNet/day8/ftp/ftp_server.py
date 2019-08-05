'''
ftp 文件服务器
'''
from socket import *
import os
import sys
import time
import signal

# 文件库路径
FILE_PATH = "/home/tarena/code/pythonNet/day8/ftp/FtpFile/"
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)

# 将文件服务器功能写在类中
class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd

    def do_list(self):
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)

        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH + file):
                files = files + file + '#'
        self.connfd.send(files.encode())


    def get_file(self,filename):
        if filename not in os.listdir(FILE_PATH):
            self.connfd.send(b"No such file.")
            return
        self.connfd.send(b'OK')
        time.sleep(0.1)
        try:
            with open(FILE_PATH + filename, 'rb') as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        time.sleep(0.1) # 防止粘包 
                        self.connfd.send(b'##')
                        break
                    self.connfd.send(data)
                    print("读取一次")
            print("文件发送完成")
        except Exception as e:
            print('error:',e)


    def put_file(self, filename):
        if filename in os.listdir(FILE_PATH):
            self.connfd.send(b"File already exists.\n")
            return
        self.connfd.send(b'OK')
        try:
            with open(FILE_PATH + filename, 'wb') as f:
                while True:
                    data = self.connfd.recv(1024)
                    if data == b'##':
                        print("\n已接收文件" + filename)
                        break
                    f.write(data)
                    print("---",end='')
        except Exception as e:
            print('error:',e)






# 创建套接字,接受客户端连接,创建新的进程
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    # 处理子进程退出
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    print("Listen the port 8000 ...")

    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("服务器异常:", e)
            continue
        print("已连接客户端:", addr)

        # 创建子进程
        pid = os.fork()
        if pid == 0:
            sockfd.close()
            ftp = FtpServer(connfd)
            # 判断客户端请求
            while True:
                data = connfd.recv(1024).decode()
                if not data or data[0] == 'Q':
                    connfd.close()
                    sys.exit("客户端退出")
                elif data[0] == "L":
                    ftp.do_list()
                elif data[0] == "G":
                    ftp.get_file(data[2:])
                elif data[0] == "P":
                    ftp.put_file(data[2:])

            sys.exit(0)
            
        else:
            connfd.close()
            continue


if __name__ == "__main__":
    main()
