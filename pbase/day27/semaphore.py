
import multiprocessing
import time

def drinkcoffee(s,i):
    s.acquire()
    print(multiprocessing.current_process().name+'get')
    time.sleep(1)
    s.release()
    print(multiprocessing.current_process().name+'release')

if __name__=='__main__':
    s=multiprocessing.Semaphore(2)

    for i in range(5):
        p=multiprocessing.Process(target=drinkcoffee,args=
            (s,i))
        p.start()
        # time.sleep(0.5)

