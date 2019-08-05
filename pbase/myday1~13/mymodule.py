# n#=input("请输入季度:")
# n=int(n)#
# if n==1:
#     print("第一季度有１，２，３月")
# elif n==2:
#    print("第三季度有７，８，９月")
#     print("第四季度有１０，１１，１２月")
# else
# n=input("请输入学生成绩：")
#n=int(n)
#if 0<=n<=100:
   # print("输入合法")
    #if 0<=n<=59:
    #    print("不及格")
   # elif 60<=n<=79:
   #     print("及格")
   # elif 80<=n<=89:
    #    print("良好")
   # else:
    #    print("优秀")
#else:
  #  print("输入不合法")
#x=input("请输入x:")
#x=int(x)
#y=input("请输入y:")
#y=int(y)
#print(x+y)
#print(x*y)
#x=float(input("请输入一个数："))
#if x>=0:
#  print(x)
#else:
#  print(-x)
#x=float(input("请输入一个数："))
#if x>=0:
#北京出租车计价器：收费标准３公里以内收费１３元，基本单价是２．３元／每公里，
#空使费：超过１５公里后，每公里加收单价的５０％空使费，相当于３．４５圆／每公里
# #要求：输入公里数，打印出费用金额，（以元为单位四舍五入）
# x=float(input("输入公里数："))
# if x<0:
#   print('输入不合法')
#   quit()
# elif x<=3:
#  print("金额为：13")
# elif x<=15:
#  y=13+(x-3)*2.3
#  y=round(y)
#  print("金额为:",y)
# else:
#  y=13+12*2.3+(x-15)*2.3*1.5
#  y=round(y)
#  print("金额为:",y)

# x=int(input("输入整数："))
# y=(x<<2)+x
# print(y) 
# x=int(input('请输入一个整数：'))
# print('%c'%x,'%d'%x,'%o'%x,'%x'%x)

# n=int(input('请输入一个数：'))
# i=0
# while i<n:
#   print('我')
#   i+=1

# i=1
# while i<=20:
#   print(i,end='　')
#   i+=1

# i=1
# while i<=20:
#   print(i,end='　')
#   if i%5==0:
#     print()
#   i+=1

# begin=int(input('输入一个开始值：'))
# end=int(input('输入一个结束值:'))
# i=begin
# while i<end:
#   print(i,end=' ')
#   i+=1
#   if (i-begin)%5==0:
#    print()

# sun=0
# i=1
# while i<=100:
#   print(i,'+',end='')
#   i+=1
#   sun+=i
# else:
#   print('和：',sum)

# n=int(input('输入：'))
# i=1
# j=1
# while j<=n:
#   while i<n+j:
#     print(i,end=' ')
#     i+=1
#   j+=1
#   i=j
#   print()

# x=(input('输入第一行：'))
# y=(input('输入第二行：'))
# z=(input('输入第三行：'))
# x1=len(x)
# y1=len(y)
# z1=len(z)
# n=max(x1,y1,z1)
# print('+'+'-'*n+'+')
# print('|'+x.center(n)+'|')
# print('|'+y.center(n)+'|')
# print('|'+z.center(n)+'|')
# print('+'+'-'*n+'+')

# x1=ord('A')
# i=1
# while i<=26:
#   print(chr(x1),end='')
#   x1+=1
#   i+=1
# print()
# x1=ord('A')
# x2=ord('a')
# i=1
# while i<=26:
#   print(chr(x1)+chr(x2),end='')
#   x1+=1
#   x2+=1
#   i+=1

# begin=int(input('请输入起始值:'))
# end=int(input('请输入终始值:'))
# print('十进制编码','十六进制编码','文字')
# while begin<=end:
#   print(' '*3,begin,' '*6,"%x"%begin,' '*6,"%c"%begin)
#   begin+=1

# i=1
# j=0
# while j<=9:
#   while i<=j:
#     print(i,'*',j,'=',i*j,sep='',end='　')
#     i+=1
#   j+=1
#   i=1
#   print()

# n=int(input('请输入一个数：'))
# for i in range(1,n+1):
#     x='*'*(i*2-1)
#     print(x.center(2*n-1))
# for j in range(1,n+1):
#     print(('*').center(2*n-1))

#算出100-1000以内的水仙花数，水仙花数是值百位的三次方＋十位的三次方＋个位的三次方
# 等于原数，
# 示例：152=1**3+5**3+3**3

# for x in range(1,10):
#     for y in range(0,10):
#         for z in range(0,10):
#            if x**3+y**3+z**3==x*100+y*10+z:
#              print(x*100+y*10+z)
# 方法２
# for x in range(100,1000):
#    s=str(x)
#    bai=int(s[0])
#    shi=int(s[1])
#    ge=int(s[2])
#    m=bai**3+shi**3+ge**3
#    if x==m:
#      print(x)


# ５．计算完全数：(是指除自身以外的所有因数之和相加，等于自身的数)
# 求４～５个完全数　
# 　　　1+2+3=6
# n=int(input('请输入范围值：'))
# for i in range(1,n+1):
#   sum=0
#   for j in range(1,i):
#     if i%j==0:
#       sum=sum+j
#   if sum==i:
#     print(i)

# l=[3.1,3.2]
# l1=[1,2,l]
# l2=l1.copy
# l[0]=3.145
# print(l1)
# print(l2)
# import copy
# l=[3,4]
# a=[1,2,l]
# b=copy.deepcopy(a)
# print(b)
# l[0]=3.14
# a.reverse()
# print(a)
# print(b)

# 已知右列表l=[3,5],用来的方法实现列表变为：
# l=[1,2,3,4,5],将列表反转，删除最后一个后打印此列表
# print[5,4,3,2]
# l=[3,5]
# l.insert(1,4)
# l.insert(0,2)
# l.insert(0,1)
# print(l)
# l.reverse()
# l.pop()
# print(l)

#[[1,2,3],[4,5,6],[7,8,9]]
l=[[x,x+1,x+2] for x in range(1,10) if x%3==1]
print(l)