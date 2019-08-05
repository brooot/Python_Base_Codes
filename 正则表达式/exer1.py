import re

f = open("test1.txt")

pattern = r"(-?\d+\.?/?\d*%?)"

pattern = '[A-Z]\w*'

regex = re.compile(pattern)

s = regex.findall(f.read())

print(s)

def get_address():
    pass



get_address()