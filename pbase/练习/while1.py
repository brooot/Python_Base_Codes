# while 0<1:
#     x=input('用户名：')
#     y=input('密码：')
#     if x=="tarena" and y=="123456":
#         print('欢迎你回来')
#         break
#     else:
#         print("错误，请重新输入！")

# i=1
# while i<=3:
#     x=input('用户名：')
#     y=input('密码：')
#     if x=="tarena" and y=="123456":
#         print('欢迎你回来')
#         break
#     else:
#         print("错误，请重新输入！")
#         i+=1
# else:
#     print('请找回密码')    

# s=input('请输入字符串：')
# i=0
# j=0
# for ch in s:
#     if ch=='a':
#         i+=1
#     if ch==' ':
#         j+=1
# print('a的个数：',i)
# print("' '的个数",j)

# for x in range(1,21):
#     print(x,end=' ')

# for x in range(1,21):
#     print(x,end=' ')
#     if x%5==0:
#         print()

# n=int(input('请输入一个数：'))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# n=int(input('请输入一个数：'))
# for i in range(1,n+1):
#     for j in range(i,n+i):
#         print(j,end=' ')
#     print()
# sum=0
# for i in range(1,100,2):
#     sum=sum+i
# print(sum)

# for x in range(5):
#     if x==2:
#         continue
#     print(x)
# else:
#     print('for循环结束')

# for i in range(1,20):
#     if i%2==0: 
#         continue
#     print(i,end=' ')

# i=1
# while i<=20:
#     if i%2==1:
#         print(i,end=' ')
#     i+=1

# n=int(input('输入一个数：'))
# if n<=1:
#     print(n,'不是素数')
#     quit() 
# for i in range(2,n):
#     if n%i==0:
#         print(n,'不是素数')
#         break
# else:
#     print(n,'是素数')

# x=input('请输入第一行：') 
# y=input('请输入第二行：')
# z=input('请输入第三行：')
# L=[x,y,z]
# print(L)

# 　经理有：曹操，刘备，周瑜
# 技术员：曹操，周瑜，张飞，赵云
# １．即是经理又是技术员
# ２．是经理，但不是技术员
# ３，是技术员，不是经理
# ４．张飞是经理吗
# ５，身兼一职的人是谁
# ６．经理和技术员共几个
# s1={'曹操','刘备','周瑜'}
# s2={'曹操','周瑜','张飞','赵云'}
# n1=s1&s2
# n2=s1-s2
# n3=s2-s1
# n4='张飞' in s1
# n5=s1^s2
# n6=s1|s2
# print(n1,n2,n3,n4,n5,n6)
# def f_outer():    #外部函数
#     print('diyibu')
#     def f_inner():  
#         print('fgftg')
#     #调用内部嵌套函数：(调用两次)
# f_outer()
#    
# def get(op):
#     def f1(x,y):
#         return x+y
#     def f2(x,y):                
#         return x*y
#     if op=='加' or op=='+':
#         return f1
#     if op=='乘' or op=='*':
#         return f2
# s=input('请输入计算公式：')
# l=s.split(' ')
# a=int(l[0])
# fn=get(l[1])
# b=int(l[2])
# print('结果是',fn(a,b))

# def hello(l):
#     for x in l:
#        print('欢迎',x)

# def f(fn,lst):
#     fn(lst)
# f(hello,['tom','jerry'])
# １．写一个函数，用列表返回n以内的菲波那数列：
# def fibonacci(n):
# 输入２０，返回[1,1,2,3,5,8,13]

# def fibonacci(n):
#     i=1
#     j=1
#     l=[1]
#     while j<=n:
#         l.append(j)
#         x=j
#         j=j+i
#         i=x 
#     return l
# n=int(input('请输入一个数：'))
# print(fibonacci(n))

# ２．用列表返回前n个菲波那数列
# def fibonacci(n):
# 输入１０，返回[1,1,2,3,5,8,13,21,34,55]

# def fibonacci2(n):
#     i=1
#     j=1
#     l=[1]
#     y=1
#     while y<n:
#         l.append(j) 
#         x=j
#         j=j+i
#         i=x 
#         y+=1
#     return l
# n=int(input('请输入一个数：'))
# print(fibonacci2(n))

# def fibonacci(n):
#     l=[1,1]
#     while l[-1]+l[-2]<n:
#         l.append(l[-1]+l[-2])
#     return l
# n=int(input('请输入一个数：'))
# print(fibonacci(n))

# l=[]
# def input_number():
#     global l
#     while True:
#         s=input('shuru')
#         if not s:
#             break
#         l.append(s)
# input_number()
# print(l)

# var=100
# def outter():
#     var=200
#     print('shuchu',var)
#     def inner():
#         var+=1
#         print('shuchu2',var)
#     print('shuchu3',var)
# print('shuchu4',var)
# outter()

# myadd=lambda x,y,z:x+y+z
# # print(myadd(10,20,30))
# print('和：',myadd(20,10,30))

# mymax=lambda x,y:x if x>y else y
# print(mymax(100,200))
# print(mymax("100",'50'))
# a=1
# b=2
# c=3
# def fn(c,d):
#     e=300
#     g=globals()
#     l=locals()
#     # print(g)
#     print(g['c'])
# fn(c,d)  

# def func(*args):
#     print(args)
# func()   #调用，不传实参
# func(1,2,3,4)

# def make_power(y):
#     def power(x):
#         return x**y
#     return power
# a=make_power(2)
# b=make_power(3)
# print(a(4))
# print(b(5))
# def power2(x):
#     return x**2
# mit=map(power2,range(1,10))
# for x in mit:
#     print(x,end=' ')
# for x in mit:
#     print(x)

# def mymul(a,b):
#     return a*b
# for x in map(mymul,range(1,5),range(4,0,-1)):
#     print(x,end=' ')

# １．求1**2+2**2+....9**2的和
# ２．求1**3+........9**3的和
# ３求1**9+2**8+....9**1的和
# def map_sum(x):
#     return x**2 
# sum=0
# for x in map(map_sum,range(1,10)):
#     sum+=x
# print(sum)
# def map_sum2(a,b):
#     return a**b

# sum=0
# for x in map(map_sum2,range(1,10),range(9,0,-1)):
#     sum+=x
# print(sum)

# print(sum(map(lambda x,y:x**y,range(1,10),range(9,0,-1))))

# print([x for x in filter(lambda y: y%2==0,range(1,21))])


# def sum_prime(x):
#     for i in range(2,x):
#         if x%i==0:
#             break
#     else:
#         return True
# print(sum(filter(sum_prime,range(3,10)))

# names=['Tom','Jerry','Spike','Tyke']

# # def k(s):
# #     return s[::-1]
# l=sorted(names,key=lambda s: s[::-1])
# print(l)
# x=100
# y=200
# s='x+y'
# a=eval(s)
# print(a)
# x=100
# y=200
# s='print("hello",x,y)'
# exec(s)

# def mysum(begin,end):
#     if begin==end:
#         return end
#     return begin +mysum(begin+1,end)
# print(mysum(1,100))
# def fn(n):
#     if n==100:
#         return 100
#     return n+fn(n+1)
# print(fn(1))
# １．编写函数fac(n)优先使用递归返回n的阶乘（n!=1*2*3..*n)
#  2.写程序算出１－２０的阶乘和

# def fac(n):
#     if n==1:
#         return 1
#     return n*fac(n-1)
# # print(fac(20))


# def sum_fac(n):
#     if n==1:
#         return 1

#     return sum(map(fac,range(1,n+1)))
# # print(sum_fac(5))

# a=100
# b=200

# m=eval('a+b')
# n=exec('a+b')
# print(m)
# print(n)

# def mydeco(fn):
#     print('fff')
#     def myfunc2():
        
#         print('123')
#     return myfunc2
# @ mydeco    
# def myfunc():
#     print('mydeco被调用')
# # myfunc=mydeco(myfunc)
# myfunc()
# myfunc()
# myfunc()
# import time
# def check_time(fn):
#     def myplay(t,f):
#         n=time.time()
#         fn(t,f)
#         n2=time.time()
#         print('总时间：',n2-n)
#     return myplay
# @ check_time
# def play(Title,frame):
#     print('正在播放：',Title,'的',frame,'帧')
#     # time.sleep(3)
#     for x in range(10000):
#         pass
# play('猫和老鼠:',1)
# play('猫和老鼠:',2)
# play('猫和老鼠:',3)
# def abc():
#     pass
# fn=abc
# print('a绑定函数名称是：',fn.__name__)
# def cba():
#     '这是cba函数的文本字符串：'
#     pass
# print(cba.__doc__)
# l=[1,2,3]
# def f(n=0,lst=[]):
#     lst.append(n)
#     print(lst)
# f(4,l)
# f(5,l)  
# f(100)
# f(200)
# f(6,l)
# １．输入一个圆的半径，求圆的周长和面积
# ２．已知一个正方形的面积为２０，求此正方形的边长，
# 　　　sqrt(x),求平方根
# import math
# r=float(input('圆的半径：'))
# s=2*r*math.pi
# s1=math.pi*r**2
# print('圆的周长：',s,'面积：',s1)

# a=math.sqrt(20)
# print('正方形边长：',a)
# import time
# year=int(input('生日：'))
# month=int(input('生日：'))
# day=int(input('生日：'))
# t=(year,month,day,0,0,0,0,0,0)
# t1=time.mktime(t)
# t2=time.time()
# t3=(t2-t1)//60//60//24
# print('出生',t3,'天')

# def sum_age(x):
#     if x==1:
#         return 10
#     return 2+sum_age(x-1)
# time.time() 　　　返回计算机元年到现在的时间秒
# time.sleep(secs)   让程序睡secs秒
# time.gmtime([secs]) 将秒数转为UTC表达的时间元组
# time.asctime([secs]) 将时间元组转为日期时间字符串
# time.mktime(tuple)   将本地时间元组转换为计算机元年秒数
# time.localtime([secs])　将UTC时间转换为本地时间元组
#(2000,12,12,23,59,59,0,0,0)
# from time import time,sleep,localtime,mktime

# while True:
#     tuple1=localtime()
#     print(tuple1[3],':',tuple1[4],':',tuple1[5])
#     sleep(1)

# 方法１
# start=int(time())
# while True: 
#     end=int(time())
#     if end-start==5:
#         print('时间到了！')
#         break
#     else:
#         sleep(1)
# 方法２

# x=input('输入时间：')
# # l=x.split(":")
# l=eval(x)
# while True: 
#     sleep(1)
#     tuple2=localtime()
#     for i in range(6):
#         if int(tuple2[i])!=int(l[i]):
#             break
#     else:
#         print('时间到了！')
#         sleep(5)
#         exit()

# print(localtime())

# 方法３
# x=input('输入时间：')
# l=eval(x)
# t1=int(mktime(l))
# while True:
#     if int(time())==t1:
#         print('时间到了！')
#         sleep(5)
#         exit()
#     else:
#         sleep(1)

# print(localtime())

# from random import randrange
# x=randrange(0,101)
# i=0
# while True:
#     i+=1
#     y=int(input('请输入一个整数：'))
#     if y==x:
#         print('恭喜你答对了')
#         print('猜的次数',i)
#         break
#     elif y>x:
#         print('你猜大了')
#     elif y<x:
#         print('你猜小了')
# R.sample(seq,n)　从序列中选择n个随机且不重复的元素

from random import shuffle
# l=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
# l1=['\u2660','\u2663','\u2665','\u2666']
# l3=['g','G']
# for i in l:
#     for j in l1:
#         l3.append(j+i)
# # print(l3)
# shuffle(l3)
# p1=l3[0:51:3]
# p2=l3[1:51:3]
# p3=l3[2:51:3]
# p4=[l3[51],l3[52],l3[53]]
# print(p1,p2,p3,p4)

kinds=['\u2660','\u2663','\u2665','\u2666']
number=['A']
number+=[str(x) for x in range(2,11)]
kinds2=['dawang','xiaowang']

l=[x+y for x in kinds for y in number]
l+=kinds2
print(l)