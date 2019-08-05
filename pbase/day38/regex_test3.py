import re
# re_obj=re.compile(r'ab',re.I)

# print(re_obj.search('Abcd').group())
s='''hello
world'''
print(re.findall(r'.*',s,re.S))

print(re.findall(r'^world',s,re.M))