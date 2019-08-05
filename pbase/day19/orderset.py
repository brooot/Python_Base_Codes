
class OrderSet:
    def __init__(self,it=None):
        if it is None:
            self.data=[]
        elif it:
            self.data=[x for x in it]
    def __repr__(self):
        return 'OrderSet(%r)'%self.data
    def __and__(self,rhs):
        return OrderSet(x for x in self.data if x in rhs.data)
    def __or__(self,rhs):
        return OrderSet(self.data+[x for x in rhs.data
        if x not in self.data])
    def __sub__(self,rhs):
        return OrderSet(x for x in self.data if x not in rhs.data)


s0=OrderSet()
s1=OrderSet([1,2,3,4])
s2=OrderSet([3,4,5])

s3=s1&s2
print(s3)

s3=s1|s2
print(s3)

s3=s1-s2
print(s3)

# s3=s1^s2
# print(s3)