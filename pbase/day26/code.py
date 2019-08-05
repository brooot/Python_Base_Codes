# from multiprocessing import Process
# import time
# def myfn1(n):
#     print("Hello,MrGreen")
# if __name__=='_main_':
#     p=Process(target=myfn1,args=(1,))
#     p.start()
#     print("I am Lucy.")

#执行结果 父进程不会等子进程
# from multiprocessing import Process
# import time

# g_num=100

# def gettime(interval):
#     global g_num
#     while True:
#         time.sleep(interval)
#         g_num += 100
#         print("in child g-num is %d"%g_num)
# if __name__ =="__main__":
#     p=Process(target=gettime,args=(2,))
#     p.start()
#     while True:
#         time.sleep(1)
#         g_num += 1
#         print("in parent g_num is %d"%g_num)
 

from multiprocessing import Pool
import os
import time

def f(x):
    print(os.getpid(), 'x =', x)
    return x*x

if __name__ == '__main__':
    p = Pool()

    #time1 = time.time();
    print(p.map(f, range(1, 6)))
    #print(time.time() - time1)    
