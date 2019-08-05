
class Myodd:
    def __init__(self,begin,end):
        if begin%2==0:
            begin+=1
        self.begin,self.end=begin,end
    def __str__(self):
        return 'Myodd(%s)'%[x for x in range(self.begin,self.end,2)]
    def __iter__(self):
        self.cur=self.begin
        return self
    def __next__(self):
        if self.cur>=self.end:
            raise StopIteration
        r=self.cur
        self.cur+=2
        return r 
# odd=Myodd(2,10)
# print(odd)
# it=iter(odd)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
for x in Myodd(2,10):
    print(x)