# -*- coding: utf-8 -*-
import multiprocessing

#消费者行为
def consumer(pipe):
    conn1,conn2=pipe
    conn2.close()
    while True:
        item=conn1.recv()
        if item==None:
            break
        print(item)
    conn1.close()

def producer(sequence,conn2):
    for item in sequence:
        conn2.send(item)

if __name__=='__main__':
    #conn1 接受数据
    #conn2 发送数据
    (conn1,conn2)=multiprocessing.Pipe()
    #创建生产消费进程
    cons_p=multiprocessing.Process(target=consumer,
        args=((conn1,conn2),))
    cons_p.start()

    conn1.close()
    sequence=[1,2,3,4,5,None]
    producer(sequence,conn2)
    
    conn2.close()
    # pro_p=multiprocessing.Process(target=producer,
    #     args=((conn1,conn2),))
