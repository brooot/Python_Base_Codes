from multiprocessing import Process, Lock
import sys
from time import sleep


def writer1():
    with lock:
        for i in range(20):
            sys.stdout.write("writer1想向终端写入\n")


def writer2():
    with lock:
        for i in range(20):
            sys.stdout.write("writer2想向终端写入\n")
    


lock = Lock()


w1 = Process(target=writer1)
w2 = Process(target=writer2)

w1.start()
w2.start()

w1.join()
w2.join()
