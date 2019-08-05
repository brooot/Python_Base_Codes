# x=1
# sum=1
# def cal(n):
#     while x<=n:
#         sum += 1/(2**n)
#         return sum
# print(cal(n))

# def cal(n):
#     result=0
#     for i in range(n+1):
#         result += 1/(2**i)
#     return result
# # n=int(input("请输入n:"))
# for i in range(10,100):
#     print(cal(i))


def cal1(n):
    result=0
    for i in range(1,n+1):
        result += 1/i
    return result
# n=int(input("请输入n:"))
for n in range(1,20):
    print(cal1(n))