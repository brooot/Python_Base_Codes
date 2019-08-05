
import random
from queue import PriorityQueue
class Taskitem(object):
    def __init__(self,name,level):
        self.name=name
        self.level=level
    #保证打印出来的格式
    def __repr__(self):
        return self.name+','+str(self.level)
    def __lt__(self,other):
        return self.level<other.level

if __name__=='__main__':
    q=PriorityQueue()
    q.put(Taskitem('watch TV',random.randint(1,20)))
    q.put(Taskitem('listen to music',random.randint(1,20)))
    q.put(Taskitem('print doc',4))
    q.put(Taskitem('write doc',4))
    while not q.empty():
        print(q.get())