
class Mynumber:
    def __init__(self,value):
        self.data=value

    def __repr__(self):
        s='Mynumber(%d)'%self.data
        return s
    def __abs__(self):
        if self.data<0:
            return Mynumber(-self.data)
        return Mynumber(self.data)
n1=Mynumber(-100)
print(n1)
n2=abs(n1)
print(n2)

# i1=int(-100)
# print(i1)
