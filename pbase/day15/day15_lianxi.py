
# s={'tom','jerry','spike','tyke'}
# for x in s:
#     print(x)
# else:
#     print('games over')

# it=iter(s)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break
# 能否用while循环来遍历range(1,10,3)返回的对象

# it=iter(range(1,20,3))
# while True:
#     try:
#         print(next(it),end=' ')
#     except StopIteration:
#         break

# １．写一个生成器函数myadd(x)用来生成x以内的奇数
# 如：myadd(10)    可以生成[1,3,5,7,9]
# 2.写一个生成器函数　myprimes(n),用来生成n以内所有素数
# 打印１００以内的素数

# def myadd(x):
#     l=[]
#     for i in range(1,x,2):
#         yield i
# x=int(input('请输入整数：'))
# l=[x for x in myadd(x)]
# print(l)

# def myprimes(n):
#     for i in range(2,n):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             yield i
# for x in myprimes(100):
#     print(x,end=' ')

# ３．写一个生成器函数myrange(),用来生成一系列整数：
# 　　　　myrange与range功能相同
# 　　　　不允许使用range和列表
def myrange(start,stop=None,step=1):
    if stop==None:
        stop=start
        start=0
    if step>0:
        while start<stop:
            yield start
            start+=step
    elif step<0:
        while start>stop:
            yield start
            start+=step
for x in myrange(10,1,-2):
    print(x,end=' ')

