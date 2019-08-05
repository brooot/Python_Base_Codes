
class Even:
    def __init__(self,begin,end):
        self.begin,self.end=begin,end
    def __str__(self):
        s='偶数'
        e=self.begin
        if e%2==1:
            e+=1
        for x in range(e,self.end,2):
            s+=" "+str(x)
        return s
    def __contains__(self,e):
        if e<self.begin:
            return False
        if e>=self.end:
            return False
        if e%2==0:
            return True
        return False
e1=Even(1,10)
print(e1)
e2=Even(0,100)
print(e2)
if 4 in e1:
    print('4在e1中')
if 100 not in e1:
    print('100不在e1')


