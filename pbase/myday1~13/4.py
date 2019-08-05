# x=float(input("输入第一个成绩:"))
# y=float(input("输入第二个成绩:"))
# z=float(input("输入第三个成绩:"))
# # if x>y:
#     if x>z:
#         print("最大值为",x) 
#         if y>z:
#             print("最小值为",z)
#         else:
#             print("最小值为",y)
#     else:
#         print("最大值为:",z) 
#         print("最小值为",y)
# elif y>z:
#     print("最大值为:",y)
#     if x>z:
#         print("最小值为",z)
#     else:
#         print("最小值为",x)    
# else:
#     print("最大值为:",z)
#     print("最小值为",x)
# print("平局值",(x+y+z)/3)
# m=x
# if y>m:
#     m=y
# if z>m:
#     m=z
# print('最大值：',m)
# n=x
# if y<n:
#     n=y
# if z<n:
#     n=y
# print('最小值：',n)
# print('平局值：',(x+y+z)/3)
# x=str(input('请输入一个字符串：'))
# y=x[::-1]
# if x==y:
#     print('回文')
# else:
#     print('不是回文')
# a='The students are sleel'

# a=str(input('请输入一个字符串'))
# print("The的个数:",a.count('The'))
# print("空格的个数:",a.count(' '))

# a=str(input('请输入一个字符串'))
# b=a[0]
# print(ord(b))

# a=int(input('请输入一个整数'))
# if 0<=a<=65535:
#      b=chr(a)
#      print(b)
# else:
#     print('输入错误！')
# fmt='姓名：%s,年龄：%d'
# n="weimingze"
# a=35
# print(fmt%(n,a))

# x=str(input('姓名：'))
# y=int(input('年龄：'))
# a='姓名：%s 年龄：%d'

# print('姓名：%s姓名：'%x,'年龄：%d年龄：'%y)
# print(a%(x,y))

# a='123sad1f  S'
# b=a.count('2')
# print(a.strip())
# c=a.find('S')+3
# print(a.center(c))

# for j in range(1,10):
#     for i in range(1,j+1):
#         print(i,'*',j,'=',i*j,end=' ',sep='')
#     print()
# (year,month,day,hour,minute,second,xinqi,yuandan,xialing)
# from time import localtime,sleep
# while True:   
#     t=localtime()
#     print('\r%d:%d:%d'%(t[3],t[4],t[5]),end=' ')
#     sleep(1)

# l=[2,7,9,5,7,4,2,5,2]
# l2=[2,1,2,1,2]
# def fn(x):
#     l1=x.copy()
#     for i in l1:
#         if x.count(i)>1:
#             x.remove(i)
#         print(x)

# def fn2(x):
#     for i in x:
#         if x.count(i)>1:
#             x.remove(i)
#         print(x)
# fn2(l2)

from time import localtime,sleep
from threading import *
def fn():
    while True:
        s=('\r%d:%d:%d')%(localtime()[3],\
            localtime()[4],localtime()[5])
        print(s,end='')
        sleep(1)

if __name__=='__main__':
    t=Thread(target=fn)
    t.start()
    t.join()

