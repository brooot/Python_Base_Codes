import threading
from time import sleep

s = None

e = threading.Event()


def bar():
    print("bar拜山头")
    global s
    s = "天王盖地虎"


def foo():
    print("说出口令就是自己人")
    sleep(2)
    if s == "天王盖地虎":
        print("我是座山雕，自己人")
    else:
        print("打死他")
    e.set()  # 等foo运行完再执行


b = threading.Thread(target=bar)
f = threading.Thread(target=foo)


def fun():
    print("呵呵..")
    sleep(1)
    global s
    s = "小鸡炖蘑菇"


b.start()
f.start()

e.wait()   # 等待foo执行完再执行后面的代码

fun()
b.join()
f.join()
