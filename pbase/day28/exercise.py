
# ３．大作业：把一个文件夹下面至少１０００个文件拷贝到另一个文件夹下面
# ，使用多进程（进程池，多线程，线程池）
# 怎么证明你拷贝的文件没有问题，
# 什么是哈希(Hash)？　
# 给一段信息做指纹：指纹是唯一的，没有碰撞


def file_copy():

    f=open(file, 'r')
    s = f.read()
    f.close()

def file_paste():
    f2=open(file2,'w')
    f2.write(s)
    f2.close()

