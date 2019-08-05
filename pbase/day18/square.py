
class Square:
    '''此类用来描述正方形，实例只有一个真是属性，
    边长length,实例面积area是虚拟出来的'''
    def __init__(self,length):
        self.length=length
    def __repr__(self):
        return 'Square(%d)'%self.length
    def __getattr__(self,name):
        print('对象没有name属性')
        if name=='area':
            return self.length**2
        raise ArithmeticError
    def __setattr__(self,n,v):
        print('__setattr__(%s,%d)'%(n,v))
        if n=='length':
            self.__dict__[n]=v
        elif n=='area':
            self.__dict__['length']=v**0.5
        else:
            raise ArithmeticError

s=Square(10)

s.area=10000
print(s.length)
print(s.area)
# print(s.cccccc)
# if hasattr(s,'aaaa'):
#     print(s.aaaa)
print(s.__dict__)