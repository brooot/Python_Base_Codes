# pi=3.1415926


# class Circle:
#     def __init__(self,r:'半径'):
#         self.r=r
#     def __repr__(self):
#         return 'Square(%d)'%self.length
#     def __getattr__(self,name):
#         if name=='area':
#             return self.r**2*pi
#         raise AttributeError
#     def __setattr__(self,n,v):

#         if n=='r':
#             self.__dict__['r']=v
#         elif n=='area':
#             self.__dict__['r']=(v/pi)**0.5
#         else:
#             raise AttributeError            


# c1= Circle(10)
# print(c1.area)

# c1.area=314.15926
# print(c1.r)

l=[[2,4,8,2],
[0,4,4,0],
[4,0,2,4],
[2,2,2,2]]
for l1 in l:

    for i in l1:
        if i==0:
            l1.remove(i)
            l1.append(0)

           
    if l1[0]==l1[1]:
        l1[0]*=2
        del l1[1]
        l1.append(0)
        if l1[1]==l1[2]:
            l1[1]*=2
            del l1[2]
            l1.append(0)
    elif l1[1]==l1[2]:
        l1[1]*=2
        del l1[2]
        l1.append(0)

 　  elif l1[2]==l1[3]:
        l1[2]*=2
        del l1[3]
        l1.append(0)
    print(l1)

