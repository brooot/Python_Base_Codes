from socket import *
import sys
import time
import os

FILE_PATH = "/home/tarena/code/pythonNet/day8/ftp/local/"


# 基本文件操作功能
class FtpClient(object):
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b"L")
        # 等待回复
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
            print("文件列表展示完毕\n")
        else:
            # 打印失败原因
            print(data)

    def get_file(self, name):
        msg = "G {}".format(name)
        print(msg)
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(1024).decode()
        if data == "OK":
            try:
                with open(FILE_PATH + name, 'wb') as f:
                    while True:
                        data = self.sockfd.recv(1024)
                        if data == b'##':
                            print("文件下载完成")
                            break
                        f.write(data)
                        print("写入一次")
            except Exception as e:
                print('error:',e)
        else:
            print(data)


    def put_file(self,filename):
        self.sockfd.send(("P " + filename).encode())
        data = self.sockfd.recv(102).decode()
        if data == 'OK':
            try:
                f = open(FILE_PATH + filename, 'rb')
                t0 = time.time()
                while True:
                    data = f.read(1024)
                    if not data:
                        time.sleep(0.1)
                        self.sockfd.send(b'##')
                        break
                    self.sockfd.send(data)
                    
                f.close()
                print("文件上传完成,耗时",int((time.time() - t0)*1000),'ms')
            except Exception as e:
                print('error:', e)
        else:
            print(data)


    def quit(self):
        self.sockfd.send(b"Q")


# 网络连接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except:
        print("连接服务器失败")
        return

    ftp = FtpClient(sockfd)  # 功能类对象
    while True:
        print("================ 命令选项 ================")
        print("================  list =================")
        print("================ get file ==============")
        print("================ put file ==============")
        print("================  quit  ================")
        print("========================================")

        cmd = input("请输入命令>>").strip()
        # if cmd not in ('list','get file', 'put file', 'quit'):
        #     print("命令输入错误,请重新输入\n")
        #     continue
        if len(cmd.split(' ')) == 2:
            filename = cmd.split(' ')[-1]

        else:
            filename = None

        if cmd == "list":
            ftp.do_list()

        elif cmd.split(' ')[0] == 'get' and filename:
            ftp.get_file(filename)

        elif cmd.split(' ')[0] == 'put' and filename and os.path.isfile(FILE_PATH + filename):
            ftp.put_file(filename)

        elif cmd == 'quit':
            ftp.quit()
            sockfd.close()
            sys.exit("Bye~")

        else:
            print("请输入正确的命令!")


if __name__ == "__main__":
    main()
