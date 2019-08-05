from multiprocessing import Event, Process
from time import sleep


def wait_event():
    print("子进程想操作临界资源")

    # 等待临界资源释放
    e.wait()

    print("子进程 开始操作临界资源，e.is_set() = ", e.is_set())   # e.is_set() 表示能否操作临界资源
    with open("file", 'r') as f:
        print("子进程 读取文件内容：", f.read())


def wait_event_timeout():
    print("我胖虎3s中内要得到临界资源")

    # 等待临界资源释放
    e.wait(3)
    if e.is_set():

        # e.is_set() 表示能否操作临界资源
        print("胖虎 开始操作临界资源，e.is_set() = ", e.is_set())
        with open("file", 'r') as f:
            print("胖虎 读取文件内容：", f.read())
    else:
        print("时间到了，胖虎很生气！")


# 创建事件
e = Event()

# 创建子进程对象
p1 = Process(target=wait_event)
p2 = Process(target=wait_event_timeout)

#  开始子进程
p1.start()
p2.start()

print("主进程 开始对临界资源操作")
with open("file", 'w') as f:
    print("主进程 操作中")
    sleep(6)
    f.write("欲练此功，必先自宫。")


# 结束事件阻塞
e.set()
print("主进程 释放临界资源")

p1.join()
p2.join()
