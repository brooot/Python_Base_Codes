from multiprocessing import Process
from multiprocessing import Value
from multiprocessing import Lock
import time

#存钱
def deposit(money,lock):
    
    for i in range(10):
        time.sleep(0.01)
        lock.acquire()   #上锁
        money.value += 1
        lock.release()   #解锁
        print("deposit",money.value)
    
    
   
#取钱
def withdraw(money,lock):
    
    for i in range(10):
        time.sleep(0.01)
        lock.acquire()
        money.value -= 1
        lock.release()
        print("withdraw",money.value)
    
    


if __name__=="__main__":

    money=Value("i",2000)
    lock=Lock()     #定义一个排他锁，互斥量
    print(money.value)
    d=Process(target=deposit,args=(money,lock))
    d.start()

    w=Process(target=withdraw,args=(money,lock))
    w.start()

    d.join()
    w.join()
    print(money.value)















