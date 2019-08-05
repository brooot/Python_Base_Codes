
class Mynumber:
    def __init__(self,value):
        self.data=value
    def __repr__(self):
        return "Mynumber(%d)"%self.data
    def __add__(self,other):
        if type(other) is int:
            return Mynumber(self.data+other)
        elif type(other) is Mynumber:
            return Mynumber(self.data+other.data)
    def __radd__(self.lhs):
        if type(lhs) is int:
            return Mynumber(self.data+lhs)
        elif type(lhs) is Mynumber:
            return Mynumber(self.data+lhs.data)
    def __sub__(self,other):
        temp=Mynumber(self.data-other.data)
        return temp
    def __mul__(self,other):
        temp=Mynumber(self.data*other.data)
        return temp

n1=Mynumber(100)
n2=Mynumber(200)
n3=n1+n2
# n3=n1.__add__(n2)
n4=n1-n2
n5=n1*n2
print(n4)
print(n5)