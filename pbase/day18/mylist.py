
# class Mynumber:
#     def __init__(self,value):
#         self.data=value
#     def __str__(self):
#         return "数字：%s"%self.data
#     def __repr__(self):
#         s='Mynumber(%d)'%self.data
#         return s
# n1=Mynumber(100)
# n2=Mynumber(200)
# print(repr(n1))
# print(str(n1))

class Mylist:
    def __init__(self,it):
        "是可迭代对象"
        self.data=[x for x in it]


    def __repr__(self):
        s='Mylist(%r)'%self.data
        return s
    def __len__(self):
        return len(self.data)
    def __bool__(self):
        for x in self.data:
            if x:
                return True
        return False


myl1=Mylist(range(0))
print(myl1)
print(bool(myl1))
if myl1:
    print('myl1是真值')
else:
    print('myl1是假值')

myl2=Mylist([])
print(myl2)
print(bool(myl2))
if myl2:
    print('myl2是真值')
else:
    print('myl2是假值')