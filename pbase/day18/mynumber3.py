
class Mynumber:
    def __init__(self,a,b):
        self.data=a
        self.name=b

n1=Mynumber(100,'zhou')

setattr(n1,'name',200)
# delattr(n1,'name')
print(n1.name)
print(getattr(n1,'name'))