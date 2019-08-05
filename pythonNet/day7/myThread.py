from threading import Thread
from time import sleep, ctime


''' 自定义线程类'''
class MyThread(Thread):
    def __init__(self,target,name = 'tedu', args = (), kwargs = {}):
        super().__init__()
        self.target = target
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args, **self.kwargs)

def player(song, sec):
    for i in range(2):
        print("Playing %s: %s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=("my love",), kwargs={"sec": 2})
t.start()
t.join()
