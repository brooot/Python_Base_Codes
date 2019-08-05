from multiprocessing import Event


# 创建事件对象
e = Event()  # 默认为阻塞

# e.set()  # 设置事件（结束阻塞）

print(e.is_set())

e.wait(3)

e.clear()

e.wait()

