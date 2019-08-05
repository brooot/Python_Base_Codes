
from socket import *
from threading import *

# BUFFERSIZE = 1024
ADDR = ('192.168.75.128',9999)
#创建和服务器端同样的套接字类型
sockfd = socket()
#向客户端发起连接请求
sockfd.connect(ADDR)

def login():
    while True:
        name=input('please input name:')
        password=input('please input password:')
        sockfd.send(name+password).encode()
        data=sockfd.recv(1024).decode()
        if name+password==data:
            while True:
                print('-------------------')
                print('query history quit')
                print('-------------------')
                x=input('请输入选择：')
                if x=='query':
                    pass
                elif x=='history':
                    pass
                elif x=='quit':
                    break
                else:
                    print('输入错误重新输入')
                    continue
        else:
            print('输入错误重新输入')
            continue                                        


def register():
    while True:
        name=input('please input name:')
        password=input('please input password:')
        pass
        if name==data1:
            login()
        else:
            print('名字已被注册，请重新输入')


while True:
    print('-------------------')
    print('login register quit')
    print('-------------------')
    x=input('请输入选择：')
    if x=='login':
        sockfd.send('login'.encode())
        login()
    elif x=='register':
        register()
    elif x=='quit':
        break
    else:
        print('输入错误重新输入')
        continue

sockfd.close()