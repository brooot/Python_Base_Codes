
class Student:
    def __init__(self,n,a,s):
        self.name=n
        self.age=a
        self.score=s
    def __str__(self):
        s='姓名：%s,年龄：%d,成绩:%d'%(self.name,self.age,self.score)
        return s
    def __repr__(self):
        s3='Student(%r,%d,%d)'%(self.name,self.age,self.score)
        return s3

name=input('请输入name:')
age=int(input('请输入age:'))
score=int(input('请输入score:'))

s1=Student(name,age,score)
# print(s1)
# print(repr(s1)) 
print(eval(repr(s1)))