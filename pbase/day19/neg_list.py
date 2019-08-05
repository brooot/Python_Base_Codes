
class Mylist:
    def __init__(self,*args):
        if args:
            self.data=[x for x in args[0]]
        else:
            self.data=[]
    def __repr__(self):
        return 'Mylist(%r)'%self.data
    def __neg__(self):
        return Mylist(-x for x in self.data)
    def 


l1=Mylist([0,2,-1,4,-5])
l2=-l1
print(l1)
print(l2)