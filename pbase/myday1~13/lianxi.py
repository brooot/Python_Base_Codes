#５．计算完全数：(是指除自身以外的所有因数之和相加，等于自身的数)
# 求４～５个完全数　
# 　　　1+2+3=6
# n=int(input('请输入范围：'))
# for j in range(1,n+1):
#     sum=0
#     for i in range(1,j):
#         if j%i==0:
#             sum+=i
#     if sum==j:
#         print(j,end=' ')

# # 3.10000以内的全部素数，并打印，（循环嵌套） 
# for j in range(2,10000):
#     for i in range(2,j):
#         if j%i==0:
#             break
#     else:
#         print(j,end=' ')

# for i in [1,2]:
#     for j in [1,2,3]:
#         print(i,j)
#         break
#     else:
#         print('for-j')
# else:
#     print('for-i')

# for i in range(100,1000):
# x=str(100)
# y1=x[0];y2=x[1];y3=x[2]
# z1=int(y1);z2=int(y2);z3=int(y3)
# if z1**3+z2**3+z3**3==x:
#     print(x,end=' ')
# else:
#     print('dff')
# l=[1,2,3,4]
# print(l[-1:-5:-1]) 
# print(l[::-1])
# L=[1,2,3,4]
# # L[1]=3.14 #索引赋值
# # print(L)

# L+=[5]
# print(L)
# l=[2,3,4]
# l[0:1]=[1.1,2,3]
# print(l)


# l=[]
# for i in range(1:6):
#     x=float(input('请输入第'+str(i)+'数：'))
#     l=l+[x]
# print(l)
# # x1=float(input('请输入第一个数：'))
# # x2=float(input('请输入第二个数：'))
# # x3=float(input('请输入第三个数：'))
# # x4=float(input('请输入第四个数：'))
# # x5=float(input('请输入第五个数：'))
# # l=[x1,x2,x3,x4,x5]
# print('最大值：',max(l))
# print('最小值：',min(l))
# print('平均值：',sum(l)/len(l))

# 输入多行文字，存入列表中，每次输入后回车算一行，任意输入多行，
#当直接输入回车（即空行时算作输入结束）
# ）１打印刚才输入的行数
# ）２按原输出的内容在屏幕上输出内容
# ）３打印你刚才共输出多少字符

# l=[]
# while True:
#     s=input('请输入：')
#     if len(s)==0:
#         break
#     l.append (s)
#     # print(l)
# print(len(l))
# sum=0
# for i in range(len(l)):
#     print(l[i])
#     sum+=len(l[i])
# print(sum)


# l=[3,5]
# l1=l+[1,2,4]
# l1.sort()
# print(l1)
# l1.reverse()
# l1.pop()
# print(l1)

# l=list('hello')
# print(l)
# print(' '.join(l))
# print('-'.join(l))

# ２．有一些数存在于列表中，如：
# l=[1,2,45,4,5.....99,98]
# 要求将列表中只出现一次的元素存入另一个列表l2
# l=[]
# while True:
#     x=input('请输入一些数：')
#     if len(x)==0:
#         break
#     l.append(x)
# l2=[]
# for y in range(len(l)):
#     if l.count(l[y])==1:
#         l2.append(l[y])
# print(l2)

#3.将10000以内的所有素数存于列表中，求这些素数的和
# l=[]
# for i in range(2,10000):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         l.append(i)
# print(sum(l))
# print(l)


# l=[x for x in range(1,101,3)]
# print(l)

# l=[[y for y in range(x,x+3)]
#         for x in range(1,8,3)]

# print(l)

# d={"name":'wemingzhe','age':35}
# print('姓名：',d['name'],sep='') 
# d={"name":'wemingzhe','age':35}
# print(d)
# 'name' in d 
# print('name' in d)

# d={"name":'wemingzhe','age':35}
# for x in d:
#     print(x)

#输入一段字符串，打印字符串出现过的字符串及出现过的次数，
# s=input('请输入一串字符：')
# d={}
# for x in s:
#     if x not in d:
#         d[x]=1
#     else:
#         d[x]+=1
# print(d)
# for x in d:
#     print(x,':',d[x],'次')

# d={x:x**2 for x in range(1,11)}
# print(d)

# １．先输入一些单词和解释，将单词作为键，将解释作为值，
# 将这些数据输入字典中，以输入单词用空结束输入，
# 然后循环提示请输入要查找的词，如果不存在于字典中提示没找到
# ，如果存在，打印解释
# d={}
# while True:
#     x=input('请输入单词：')
#     y=input('请输入解释')
#     if len(x)==0:
#         break
#     d[x]=y
# while True:
#     z=input('请输入要查找的词：')
#     if z in d:
#         print(d[z])
#     else:
#         print('不存在于字典中')
        
#任意输入一些单词，存入集合中，当输入0时，结束输入，
# 打印输入的单词种类（去重），每种单词打印在终端上，
# 打印输入的种类数
# s=set()
# while True:
#     x=input('输入：')
#     if x=='0': 
#         break
#     s.add(x)
# print('种类数：',len(s))
# for i in s:
#     print(i)

# def say_hello():
#     print('hello',end=' ')
#     print('word')
#     return 200
#     print('wo')
# r=say_hello()
# print(r)

# def mysum(a,b):
#     c=a+b
#     print('c=',c)
# r=mysum(100,200)
# print(r)

 
# x=int(input('请输入第一个：'))
# y=int(input('请输入第二个：'))
# print('你输入数的和为：',myadd(x,y))

# １，写一个函数，mymax,实现返回三个数的最大值，如
# def mymax(a,b,c):
# def mymax(a,b,c):
#     t=a
#     if b>t:
#         t=b
#     if c>t:
#         t=c
#     return t
# x=input('请输入第一个值：')
# y=input('请输入第二个值：')
# z=input('请输入第三个值：')
# print('最大值：',mymax(x,y,z))

# def mymax2(a,b,c):
#     t=a
#     if b>t:
#         t=b
#     if cint
#         t=c
#     return t
# x=int(input('请输入第一个值：'))
# y=int(input('请输入第二个值：'))
# z=int(input('请输入第三个值：'))
# print('最大值：',mymax2(x,y,z))

# ２．定义两个函数：
# sum3(a,b,c)  用于返回三个数和
# pow3(x)　　　　返回x的三次方
# １）计算１的立方＋２的立方＋３的立方和
# ２）计算１＋２＋３的和的立方，即（１＋２＋３）**3

# def sum3(a,b,c):
#     return a+b+c
# def pow3(x):
#     return x**3
# x=pow3(1)+pow3(2)+pow3(3)
# print(x)
# y=(sum3(1,2,3))**3
# print(y)

# def myfun1(a,b,c):
#     print('a绑定：',a)
#     print('b绑定：',b)
#     print('c绑定：',c)

# # myfun1(b=222,c=333,a=111)
# d={'a':1,'b':2,'c':3}
# myfun1(**d)
# l=[]
# def fn(x):
#     x.append(10)
# fn(l)
# print(l)
# def splice_odd_even(l,o,e):
#     for i in l:
#         if i%2==1:
#             o.append(i)
#         else:
#             e.append(i)
# l=[1,3,8,7,4,1]
# odd=[]
# even=[]
# splice_odd_even(l,odd,even)
# print(odd)
# print(even) 
# def minmax(x,y,z):
#     a=min(x,y,z)
#     b=max(x,y,z)
#     return (a,b)

# x=int(input('请输入：'))
# y=int(input('请输入：')) 
# z=int(input('请输入：'))
# a,b=minmax(x,y,z)
# print((a,b))
# print(a)
# print(b) 

# def input_number():
#     l=[]
#     while True:
#         x=input('请输入整数：')
#         if x=='':
#             break
#         else:
#             l.append(int(x))
#     return l
# l=input_number()
# print(l)
# def func(*args):
#     print(args)
# func()
# func(1,2,3,4)
# def mysum(*args):
#     s=0
#     for x in args:
#         s+=x
#     return s
# print(mysum(1,5,3,6))

# def func(**kwargs):   #kwargs   keywords argument
#     print('参数个数：',len(kwargs))
#     print(kwargs)
# func(a=1,b=2,c=3)

# ２．写一个myrange函数，参数可以传１－３个，实际意义与range函数规则相同
# ，此函数返回range规则的列表
# def myrange(*args):
    




# def myrange(start,stop=None,step=1):
#     if stop is None:
#         stop=start
#         start=0
#     l=[]
#     if step>0:
#         while start<stop:
#            l.append(start)
#             start+=step
#     else:
#         while start >stop:
#             l.append(start)
#             start+=start
#     return l

# def isprimes(x):
#     for i in range(2,x):
#         if not x%i:
#             print(x,'不是素数')
#             break
#     else:
#         print(x,'是素数')
# isprimes(30)

# ２．写一个函数prime_m2n(m,n),返回从m开始到n结束（不包含n）范围内素数的列表，并打印如：
# l=prime_m2n(5,20)
# print(l)  [5,7,11,13,17,19]
# def prime_m2n(m,n):
#     l=[]
#     for i in range(m,n):
#         for j in range(2,i):
#             if not i%j:
#                 break
#         else:
#             l.append(i)
#     return l

# l=prime_m2n(5,20)
# print(l)

# 4.给出一个数n,写一个函数计算1+2**2+3**3...+n**n
# def sum_cheng(x):
#     sum=0
#     for i in range(1,x+1):
#         sum+=i**i
#     return sum
# print(sum_cheng(3))

# import time
# def myfn(n):
#     """　myfn 函数是输出n遍'
#     hello world',
#     n 作为参数"""
#     print('hello world')
#     time.sleep(1)
#     if n==1:
#         return None
#     return myfn(n-1)
# myfn(10)
