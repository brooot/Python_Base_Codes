
import time
class Cooker:
    def __init__(self,n):
        self.count=n
    def open_gas(self):
        print('正在打开天然气')
    def close_gas(self):
        print('正在关闭天然气')
    def do_works(self):
        for i in range(self.count):
            print('正在制作',i,'个并')
            time.sleep(0.5)
    def __enter__(self):
        self.open_gas()
        return self
    def __exit__(self,exc_type,exc_value,exc_tb):
        self.close_gas()

with Cooker(10) as feng:
    feng.do_works()
# feng.close_gas()
