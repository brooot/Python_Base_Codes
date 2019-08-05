import os
import time
print("hello")
pid=os.fork()

if pid <0:
    print("fork error")
elif pid==0:
    #返回值为零,是子进程的逻辑
    time.sleep(1)
    print("child id is %d,parent id is %d"%(os.getpid(),os.getppid()))
else:
    #返回值大于0,是主进程的逻辑
    print("parent id is %d,child id is %d"%(os.getpid(),pid))

