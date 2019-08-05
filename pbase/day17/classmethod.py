
class Member:
    apples=10
    def __init__(self,n):
        self.name=n
    def eat(self,count):
        print(self.name,'chile',count,'个苹果')
        self.__class__.apples-=count
    @classmethod
    def get_apple_count(cls):
        return cls.apples
    # def apple_count(self):
    #     return self.__class__.apples
print('开餐前有',Member.get_apple_count())
m1=Member('老魏')
m2=Member('老冯')
m1.eat(1)
m2.eat(2)
print('开餐hou',Member.get_apple_count())
# print(m1.apple_count())