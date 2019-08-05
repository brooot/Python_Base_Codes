from multiprocessing import Process 
from multiprocessing import Value　# 类

import time

#存钱
def deposit(money):
    for i in range(100):
        time.sleep(0.01)
        money.value += 1
   
#取钱
def withdraw(money):
    for i in range(100):
        time.sleep(0.01)
        money.value -= 1


if __name__=="__main__":

    money=Value("i",2000)
    print(money.value)
    d=Process(target=deposit,args=(money,))
    d.start()

    w=Process(target=withdraw,args=(money,))
    w.start()

    d.join()
    w.join()
    print(money.value)















