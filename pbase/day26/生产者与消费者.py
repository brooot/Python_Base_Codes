from multiprocessing import Queue
from multiprocessing import Process
import os
import time

#消费者逻辑
def consumer(q):
    while True:
        item = q.get()
        #使用None
        if item==None:
            break
        print("pid is %d %d"%(os.getpid(),item))

def producer(sequence,q):
    for i in sequence:
        q.put(i)
    q.put(None)
    q.put(None)
    q.put("A")
    q.put("B")

if __name__=="__main__":
    q=Queue()
    cons_p=Process(target=consumer,args=(q,))
    cons_p.start()
    cons_p2=Process(target=consumer,args=(q,))
    cons_p2.start()

    sequence = [1,2,3,4,5,6,7,8,9,10]
    # producer(sequence,q)
    prod_p=Process(target=producer,args=(sequence,q,))
    prod_p.start()

    cons_p.join()
    cons_p2.join()
    prod_p.join()

    print("in parent",q.get())
    print("in parent",q.get())





