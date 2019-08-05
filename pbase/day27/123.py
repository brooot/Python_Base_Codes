
# 1.存在字符串“ab2b3n5n2n67mm4n2”,
# 编程统计字符串中字母n出现的次数
# s='ab2b3n5n2n67mm4n2'
# a=s.count('n')
# print(a)
# 2.定义一个类Human, 分别有属性姓名年龄和电话（name,age,tel）
# 类中定义三个方法，分别获取name,age,和tel（5分）

# class Human:
#     def __init__(self,name,age,tel):
#         self.name=name
#         self.age=age
#         self.tel=tel
#     def getname(self    ):
#         return self.name

# m=Human('tom',34,2434)
# print(m.getname())
def f(x):
    if x==1:
        return 10

    return 2+f(x-1)
print(f(5))