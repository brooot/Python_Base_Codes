import gevent
import sys
from gevent import monkey
from time import sleep
monkey.patch_all()
def foo(a):
    print('running in foo',a)
    gevent.sleep(3)
    print('switch to foo again')

def bar():
    print('running in bar')
    gevent.sleep(2)
    print('switch to bar again')

f = gevent.spawn(foo,666)
b = gevent.spawn(bar)

gevent.joinall([f,b])