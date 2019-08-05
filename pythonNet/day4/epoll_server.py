
“”“
    poll 和 epoll的区别：
    1、epoll 效率比poll高，不用不断轮巡查看触发
    2、epoll 事件触发方式更多

    用法基本相同
”“”
from socket import *
from select import *

# 创建套接字作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

# 创建poll对象
p = epoll()  # 创建对象处 poll() 该为epoll()

# fileno -->IO对象的字典 (IO地图)
fdmap = {s.fileno(): s}

# 注册关注的IO
p.register(s, EPOLLIN | EPOLLERR)

while True:
    # 进行IO监控
    events = p.poll()  # 此处不用改
    for fd, event in events:  # events = [(套接字.fileno(), event),...]
        if fd == s.fileno():  # 有新的客户端连接
            c, addr = fdmap[fd].accept()
            print("Connect from", addr)
            p.register(c, EPOLLIN | EPOLLHUP)  # 关注的对象处前面加E
            fdmap[c.fileno()] = c  # 添加客户端连接套接字到IO地图
        elif event & EPOLLIN:  # 表示有客户端发来消息
            data = fdmap[fd].recv(1024)
            if not data:
                # 客户端退出，从关注事件移除
                p.unregister(fd)
                print(fdmap[fd].getpeername(), 'disconnected')
                fdmap[fd].close()
                # 从io地图中移除
                del fdmap[fd]
            else:
                print(data.decode())
                fdmap[fd].send(b'Message received')
