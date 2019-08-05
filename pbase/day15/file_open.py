
try:
    f=open('./myfile.txt')
    print('文件打开')

    f.close()
    print('文件关闭了')
except:
    print('文件打开失败')