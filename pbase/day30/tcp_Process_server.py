from socket import *
import traceback
import os
import sys
from signal import *

host = '0.0.0.0'
post = 8888
BUFFERSIZE = 1024
addr = (host,post)
  
s = socket()
s.bind(addr)
s.listen(5)
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    print('connect from',c.getpeername())
    #处理僵尸进程
    signal(SIGCHLD,SIG_IGN)
    pid = os.fork()
    if pid < 0:
        print('create child process error')
        continue
    elif pid >0:
        c.close()
        continue
    else:
        s.close()
        while True:
            data = c.recv(BUFFERSIZE).decode()
            if not data:
                break
            print(data)
            c.send('receive your message'.encode())
        c.close()
        sys.exit(0)
s.close()


