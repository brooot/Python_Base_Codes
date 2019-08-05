from multiprocessing import Process
import time

def DoPut(l):
    for i in range(10):
        l.append(i)
    print("DoPut over")

if __name__=='__main__':

    l=[]
    p=Process(target=DoPut,args=(l,))
    p.start()

    time.sleep(2)
    for i in l:
        print(i)
    print("l lenth is ",len(l))