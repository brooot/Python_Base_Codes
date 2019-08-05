
class Mylist:
    def __init__(self,*args):
        if args:
            self.data=[x for x in args[0]]
        else:
            self.data=[]
    def __repr__(self):
        return 'Mylist(%r)'%self.data
    def __add__(self,other):
        if type(other) is int:
            return Mylist(self.data+[other])
        elif type(other) is Mylist:
            return Mylist(self.data+other.data)
    def __radd__(self,lhs):
        if type(lhs) is int:
            return Mylist(self.data+[lhs])
        elif type(lhs) is Mylist:
            return Mylist(self.data+lhs.data)

l1=Mylist(range(3))
l2=Mylist([3,4,5])
l3=l1+l2
print(l3)
l3=l3+6
print(l3)
l3=7+l3
print(l3)
l3+=8
print(l3)
# l1*=2
# print(l1)