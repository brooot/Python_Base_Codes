from multiprocessing import Queue
from time import sleep

#  创建队列
q = Queue(3)

q.put([2,4])
sleep(0.2)
print(q.empty())
q.put(2)
q.put(3)
print(q.full())
print(q.qsize())

print(q.get())
print(q.get())
print(q.get())
# q.put(4,False,3)