
'''创建自定义进程类
        1、继承Process
        2、编写自己的__init__，同时加载父类init方法
        3、重写run方法，可以通过生成的对象调用start自动运行

'''


from multiprocessing import Process
import time


class ClockProcess(Process):
    def __init__(self, value):
        self.value = value
        super().__init__()  # 调用父类初始化函数

    # 重写run方法
    def run(self):
        for i in range(5):
            print("The time is{}".format(time.ctime()))
            time.sleep(self.value)


# 创建自定义进程类的对象
p = ClockProcess(2)

# 自动调用run
p.start()
p.join()
