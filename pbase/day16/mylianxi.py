
# f=open('mylianxi.txt','r')
# s=f.read()
# f.close()
# alpha=s[::2]
# number=s[1::2]
# print(alpha)
# print(number)

# s='A1B2C3D4'
# f=open('mylianxi.txt','w')
# f.write(s)
# f.close()

# f=open('mylianxi.txt','r+b')
# b=f.read()
# ba=bytearray(b)
# ba[::2]=[ord(x) for x in 'ABCD']
# f.seek(0)
# f.write(ba)
# f.close()
# print(b)


# f=open('sublimetext3.txt','w')

# while True:
#     s=input('请输入：')
#     if not s:
#         break
#     f.write(s+'\n')
# f.close()
f=open('infos.csv','w')

while True:
    s=input('请输入：')
    if not s:
        break
    b=s.encode('utf-8')
    b1=b.decode('GBK')
    f.write(b1+'\n')
f.close()
