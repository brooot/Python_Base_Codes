
from socket import *
# 创建套接字对象
sockfd = socket(AF_INET, SOCK_STREAM)


# 设置端口立即释放
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 套接字属性
# print(sockfd.family)
# print(sockfd.fileno())
# print(sockfd.getpeername())


# 套接字对象绑定（地址，端口）
sockfd.bind(('0.0.0.0', 8888))

# 设置套接字监听队列
sockfd.listen(6)

T = 1
while T:
    print('waiting for connection ...')
    # 套接字接受阻塞，并获取客户端连接套接字与客户端地址
    connfd, addr = sockfd.accept()
    print('connected from ', addr)

    print('waiting message ...')
    while True:
        # 从客户端连接套接字中获取数据
        data = connfd.recv(1024).decode()
        if data == '##':
            print('客户中断了连接。\n')
            break
        # print('\nmessage received.')
        print("client:", data)

        # 通过客户端连接套接字发送数据到客户端
        m = input("server:").encode()
        if m == b'exit':
            T = 0
            print('服务器终止了连接。')
            connfd.send(m)
            break
        connfd.send(m)
        # print('发送了',n,'个字节')

    # 关闭连接套接字
    connfd.close()

# 关闭套接字
sockfd.close()
