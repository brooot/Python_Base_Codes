
# 实现两个文件的复制，要求用with语句，打开和关闭文件
# 在复制文件时，要处理所有的异常状态

with open('one.txt','r') as f1,open('two.txt','w') as f2:
    s=f1.read()
    f2.write(s)

print('finally')
