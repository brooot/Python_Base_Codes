# 1.写一个类Myprimes,实现迭代器协议，让类能生成从b开始到e结束的
# 全部素数
# class Myprimes:
#     def __init__(self,b,e):
#         ..
#     def __iter__(self):
#       ..
#     def __next__(self):
# l=[x for x in Myprimes(10,20)]
# print(l)  #[11,13,17,19]
def isprime(x):
    if x<=1:
        return False
    for i in range(2, x):
            if x%i == 0:
                return False
    return True

class Myprimes:

    def __init__(self, b, e):
        self.begin, self.end = b, e

    def __iter__(self):
        self.cur_value = self.begin
        return self

    def __next__(self):
        for x in range(self.cur_value,self.end):
            if isprime(x):
                self.cur_value=x+1
                return x
        raise StopIteration


l=[x for x in Myprimes(10,20)]
print(l)

# p1=Myprimes(10,20)
# for x in p1:
#     print(x)

# class Mylist:

#     def __init__(self,it = None):
#         if it:
#             self.data=[x for x in it]
#         else:
#             self.data = []
#     def __repr__(self):
#         return 'Mylist(%r)'%self.data


# l=Mylist(range(5))
# print(l)