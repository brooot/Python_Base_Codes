import re

pattern = r"(ab)c(de)f"
s = 'abcdefghijklmnabcdefghi'

#re模块直接调用
l = re.findall(pattern,s)
print(l)



#compil对象调用
regex = re.compile(pattern)
l = regex.findall(s)
print(l)

print("==================================")

l = re.split(r"\s+","Hello  world nihao China")
print("split():",l)

s = re.sub(r"\s+",'#',"Hello  world   nihao China",2)
print("sub():",s)