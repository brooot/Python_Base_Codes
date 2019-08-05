
from threading import Thread
import time

def f1():
    g_num = 100
    g_num += 1
    time.sleep(3)
    print('g_num in f1 is %d'%g_num)

def f2():
    g_num = 100
    # time.sleep(3)
    print('g_num in f2 is %d'%g_num)

if __name__ == "__main__":
    t1 = Thread(target=f1)
    t1.start()
    t1.join()

    t2 = Thread(target=f2)
    t2.start()

