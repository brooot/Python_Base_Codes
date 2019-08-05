from multiprocessing import Process
import time

class myTimer(Process):
    def __init__(self, interval):
        # 需要调用父类的构造
        Process.__init__(self)
        self.interval = interval

    def run(self):
        while True:
            time.sleep(self.interval)
            print(time.ctime())


if __name__ == '__main__':
    t = myTimer(2)
    t.start() # 父类的start方法会去调用run方法，
    # 我们只需要在我们自定义的子类中重写一下run方法就可以
