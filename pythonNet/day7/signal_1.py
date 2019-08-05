from signal import *
import time


def handler(sig, frame):
    # print("signal receved")
    if sig == SIGALRM:
        print("alarm receved")
    elif sig == SIGINT:
        print("就不结束")

# 放置一个5s后发出的alarm时钟信号
alarm(5)


#设置信号监听
signal(SIGALRM, handler)
signal(SIGINT, handler)

while True:
    print("waiting for a signal")
    time.sleep(2)