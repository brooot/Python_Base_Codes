
f=open('binary_input.txt','rb')
print('刚打开的读写位置：',f.tell())

s=f.read(5)
print(s)
print('当前读写的位置',f.tell)
f.close()



f=open('binary_input.txt','r+b')
pos=f.seek(10)
print('当前读写位置：')
f.write(b'abcde')
pos=f.tell()

f.close()


