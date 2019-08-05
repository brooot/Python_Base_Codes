
class Mylist:
    def __init__(self,it):
        self.data=list(it)

    def __repr__(self):
        return "Mylist(%r)"%self.data
    def __getitem__(self,i):
        print(i)
        return self.data[i]
    def __setitem__(self,i,val):
        if isinstance(i,int):
            self.data[i]=val
        elif isinstance(i,slice):
            self.data[i]=val.data
    def __delitem__(self,i):
        del self.data[i]



myl1=Mylist(range(5,10))
# print(myl1)
# x=myl1[1]
# print(x)
# myl1[0]=10000
# print(myl1)
# del myl1[0]
# print(myl1)
myl2=myl1[0:5]
print(myl2)
myl1[0:2]=myl1([9,8])
# myl1[0]=10000
print(myl1)