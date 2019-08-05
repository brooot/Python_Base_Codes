from multiprocessing import Process
import time
class mytime(Process):

    def __init__(self,interval):
        Process.__init__(self)
        self.interval=interval

    def run(self):
        while True:
            time.sleep(self.interval)
            print(time.ctime(),"休息一下")
if __name__=="__main__":
    t=mytime(2)
    t.start()      #父类的start方法会去调用run方法