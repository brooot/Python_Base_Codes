from multiprocessing import Process
import time
import os

def getTime(interval):　
    """
    每隔interval秒,打印一下当前的系统时间
    """
    while True:
        time.sleep(interval)
        print(time.ctime())
        print("Child Process id %d"
            %os.getpid())

if __name__ == '__main__':
    # 在主进程中创建一个子进程,
    # 进程的target是进程的函数入口
    # 进程的参数args是一个元组
    p = Process(target=getTime, args=(1,))

    # 就绪
    p.start()

    # join放这，主进程下面的逻辑没有机会被执行
    #p.join()

    # while True:
    #     time.sleep(2)
    #     print("Parent Process id %d"
    #             %os.getpid())

    #p.join()
    print("Parent over")


