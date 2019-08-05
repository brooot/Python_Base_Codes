from socket import *
from select import *

# 创建套接字作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

# 创建poll对象
p = poll()

# fileno -->IO对象的字典 (IO地图)
fdmap = {s.fileno(): s}

# 注册关注的IO
p.register(s, POLLIN | POLLERR)

while True:
    # 进行IO监控
    events = p.poll()
    for fd, event in events:  # events = [(套接字.fileno(), event),...]
        if fd == s.fileno():  # 有新的客户端连接
            c, addr = fdmap[fd].accept()
            print("Connect from", addr)
            p.register(c, POLLIN | POLLHUP)  # 注册IO监控
            fdmap[c.fileno()] = c  # 添加客户端连接套接字到IO地图
        elif event & POLLIN:  # 表示有客户端发来消息
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
