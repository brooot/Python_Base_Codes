import gevent

def foo(a,b):
    print('a=%d,b=%d' % (a,b))
    gevent.sleep(2)
    print('running foo again')


def bar():
    print()