
# １．一个球从１００米高空落下，每次落地后反弹高度为原来的一半，
# 写程序算出球第１０次落地后的反弹高度和此球共经过多少米
# ２．分解因数，输入一个正整数，分解质因数，如输入：９０，则打印
# '90=2*3*3*5'

 
# def high(n)->('次数'):
#     return 100*0.5**n
# def sum_high(n):
#     if n==1:
#         return 150
#     return high(n)*3+sum_high(n-1)

# print(high(10))
# print(sum_high(10))


# def sum_high2(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=3*100*0.5**i
#     return sum
# print(sum_high2(10))


# def yinshu(n):
#     l=[]
#     m=n
#     while m!=1:
#         for j in range(2,n+1):
#             if m%j==0:
#                 l.append(str(j))
#                 m=m/j
#                 break
#     return l

# s=str(90)+'='
# s2='*'.join(yinshu(90))
# print(s+s2)

def zys(n):
    for x in range(2,n):
        if n%x==0:
            return [x]+zys(int(n//x))
    if n==1:
        return []
    else:
        return[n]
print(zys(90))