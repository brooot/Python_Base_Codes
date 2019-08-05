
# def event(begin,end):
#     start=begin
#     while start<end:
#         if start%2==0:
#             yield start
#         start+=1
#     return '不能再生产偶数了'
# # l=[x for x in event(10,20)]
# # print(l)
# gen=event(5,10)
# print(next(gen))
# print(next(gen))
# print(next(gen)) 

# gen=(x**2 for x in range(1,5))
# it=iter(gen)
# next(it)

# l=[1,3,5,7,9]
# gen=[x**2 for x in l]
# gen2=(y+1 for y in gen)
# # for z in gen2:
# #     print(z)
# print(next(gen2))
# print(next(gen2))

# numbers=[10086,10000,10010,95588]
# names=['中国移动','中国电信','中国联通']
# for i in zip(numbers,names):
#     print(i)
# d=dict(zip(numbers,names))
# print(d)


# names=['中国移动','中国电信','中国联通']
# for x in enumerate(names,1):
#     print(x)
l=[]
while True:
    x=str(input('请输入文字：'))
    if x=='':
        break
    l.append(x)
for index,x in enumerate(l,1):
    print(index,x)
