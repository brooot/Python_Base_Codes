from multiprocessing import Pool
import time
import os

def cFun(args):
    print("callback ", os.getpid(), args)

# 多进程的逻辑入口
def func(str):
    print("Pool:", str, os.getpid())
    time.sleep(2)
    print("Pool:", str, os.getpid(), "end")
    return str+"funcallback"

if __name__ == '__main__':
    # 创建进程池
    p = Pool()

    # 分配四个任务
    for i in range(4):
        msg = "apply %d"%(i)
        p.apply_async(func, (msg,),callback=cFun) #阻塞方式
        # 最好别使用这种方式，它和单进程几乎差不多

    #p.close()
    #p.join()

    #print("Main end")
    while True:
        time.sleep(2)
        print("Main Proc", os.getpid())