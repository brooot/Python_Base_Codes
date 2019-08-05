import re
# pattern=r'\w+'
# pattern=r'\s'
#获取正则表达式对象
# re_obj=re.compile(pattern)
s='hello word'
# l=re_obj.findall(s)
# print(l)
# print(dir(re_obj))
# for i in re_obj.finditer(s):
#     print(i.group())
# l1=re.split('\s',s)
# print(l1)

s1=re.sub(r'[A-Z]','***','Hello Word Love China',3)
print(s1)
s2=re.subn(r'[A-Z]','***','Hello Word Love China')
print(s2)