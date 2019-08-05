# １类似ＱＱ群聊，在聊天室中允许多个用户加入聊天室
# ２．加入一个简单的用户注册（不需要数据库，临时存储即可）
# ３.客户端发送消息时，其他客户端可以收到，但是本人收不到，收到的
# 消息是　　name say message
# 4.如果有用户进入聊天室或退出聊天室，其他客户端收到通知
# 　　name login  
#   name logout
# 5.支持管理员喊话，server发送消息
from socket import * 
from threading import Thread
from time import sleep

s=socket()
s.bind(('192.168.75.128',9999))
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.listen(5)

l = []
def handler(x):
    
    print('connect from',x.getpeername())
    name=x.recv(1024).decode()
    # connfd.send('your are ok'.encode())
    while True:
        data = x.rec v(1024).decode()
        if not data:
            break
        # print(data)
        for i in l:
            if i != x:
                i.send(('%s say: %s'%(name,data)).encode())
    for i in l:
        if i != x:
            i.send(('%s quit'%name).encode())
    l.remove(x)
    t.join()
    connfd.close()
def server_send():
    while True:
        g=input('server输入：')
        for i in l:
            i.send('server say: %s'%g.encode())

        
while True:
    try:
        connfd,addr=s.accept()
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(e)
        continue
    l.append(connfd)
    t = Thread(target=handler,args=(connfd,))
    t.start()

s.close()
