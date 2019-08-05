
from multiprocessing import Array,Process

def trans(a,size):
    for i in range(size):
        print('没有复制前的值',a[i])
    for i in range(size):
        a[i]=i
    for i in range(size):
        print('复制hou的值：',a[i])

if __name__=='__main__':
    num=10
    #定义一个长度为num的共享内存数组
    a=Array('f',num)
    p=Process(target=trans,args=(a,num))
    p.start()

