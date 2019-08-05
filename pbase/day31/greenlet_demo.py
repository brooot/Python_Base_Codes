from greenlet import greenlet

def test1():
    print(1111)
    gr1.switch()
    print(2222)
    gr2.swich()
def test2():
    print(333)
    gr1.swich()
    print(444)
#将函数注册为greenlet
gr1=greenlet(test1)
gr2=greenlet(test2)
#启动协程函数
gr1.swich()