
# class Human:
#     def say(self,what):
#         print('说',what)
#     def run(self,speed):
#         print('正在以%s速度跑'%speed)
# h1=Human()
# h1.say("今天北京天气不好")
# h1.run(120)

# class Student(Human):

#     def study(self,what):
#         print('正在学：',what)
# s1=Student()
# s1.say("今天shanghai天气不好")
# s1.run(130)

# class Teacher(Human):  
#     def teach(self,what):
#         print('老师正在教',what)
# s1=Teacher()
# s1.say("今天guanzhou天气不好")
# s1.run(140)

class A:
    def mymethod(self):
        print('A.mymethod被调用')
class B(A):
    def mymethod(self):
        print('B.mymethod被调用')
b=B()
# b.mymethod()
super(B,b).mymethod()
# A.mymethod(b)
# B.__base__.mymethod(b)