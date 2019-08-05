from socket import *
from select import select

# 创建套接字作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.bind(('127.0.0.1', 8888))
s.listen(5)

rlist = [s]  # 读IO列表
wlist = []  # 写IO列表
xlist = []  # IO异常列表

while True:
    # 提交我们关注的IO等待IO发生
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("connect from", addr)
            rlist.append(c)
        else:
            data = r.recv(1024)
            if not data:
                print("Disconnected from", r.getpeername())
                rlist.remove(r)
                r.close()
            else:
                print(data.decode())
                # 将客户端套接字放入wlist列表（放入wlist的对象会被立即提取出来执行）
                wlist.append(r)

    for w in ws:
        w.send(b"reveice your message")
        wlist.remove(w)

    for x in xs:
        pass

