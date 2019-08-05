import signal
from time import sleep

signal.alarm(3)

# 使用默认方法处理信号
# signal.signal(signal.SIGALRM, signal.SIG_DFL)

# 忽略信号
signal.signal(signal.SIGALRM, signal.SIG_IGN)
signal.signal(signal.SIGINT, signal.SIG_IGN)   # 忽略 ctrl + c 


while True:
    sleep(1)
    print("按ctrl+c 结束")
    print("等待时钟信号")