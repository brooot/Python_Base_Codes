from multiprocessing import Pool
import time

# 多进程的逻辑入口
def func(str):
    print("Pool:", str)
    time.sleep(2)
    print("Pool:", str, "end")

if __name__ == '__main__': 
    # 创建进程池
    p = Pool()

    # 分配四个任务
    for i in range(4):
        msg = "apply %d"%(i)
        p.apply(func, (msg,)) #阻塞方式
        # 最好别使用这种方式，它和单进程几乎差不多

    p.close()
    p.join()

    print("Main end")