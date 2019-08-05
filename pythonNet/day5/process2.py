from multiprocessing import Process
from time import sleep
import os

def th1():
    sleep(3)
    print("eat")
    print(os.getppid(), "--------", os.getpid())

def th2():
    sleep(3)
    print("sleep")
    print(os.getppid(), "--------", os.getpid())


def th3():
    sleep(3)
    print("study")
    print(os.getppid(), "--------", os.getpid())

things = [th1,th2,th3]
process = []

for th in things:
    p = Process(target = th)
    process.append(p)
    p.start()

for i in process:
    i.join()