import re

s = '''hello world
hello kitty
你好, 北京'''

pattern = r"^你好"

regex = re.compile(pattern, flags = re.M)


try: 
    s = regex.search(s).group()

