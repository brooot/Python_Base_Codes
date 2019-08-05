
class Car:
    pass
    def __init__(self,c,b,m):
        self.color=c
        self.brand=b
        self.model=m
        print('__init__已经被调用：',c,b,m)
    def run(self,speed):
        print(self.color,'的',self.brand,self.model,'正在以',speed,'行驶')
    def changecolor(self,c):
        self.color=c
a4=Car('红色','奥迪','A4')
a4.run(199)
a4.changecolor('黑色')
a4.run(230)