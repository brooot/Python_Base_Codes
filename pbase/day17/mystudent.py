
class Student:
    pass
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def show_info(self):
        print('name:',self.name,'age:',self.age,'score:',self.score)


def input_info():
    l=[]
    while True:
        x=input('name:')
        if not x:
            break
        y=input('age:')
        z=input('score:')
        l.append(Student(x,y,z))
    return l
docs=input_info()
print(docs)
def show(l):
    for x in l:
        x.show_info()
show(docs)