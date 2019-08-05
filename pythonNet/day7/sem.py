from multiprocessing import Semaphore, Process
from time import sleep
import os

sem = Semaphore(3)

def fun():
    sem.acquire()
    print("%s 抢到一个信号量" % os.getpid())
    sleep(3)
    sem.release()
    print("%s 释放了一个信号量" % os.getpid())


jobs = []

for i in range(4):
    p = Process(target = fun)
    p.start()
    jobs.append(p)


for i in jobs:
    i.join()


print("现在有%s个信号量" % sem.get_value())