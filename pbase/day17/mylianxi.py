
src=input('请输入源文件')
dst=input('请输入目标文件')
f_src=open(src,'rb')
f_dst=open(dst,'wb')
while True:

    b=f_src.read(4096)
    if not b:
        break
    f_dst.write(b)
f_src.close()
f_dst.close()
