import re
# re_obj=re.compile(r'foo')

# match_obj=re_obj.match('fooThis is my foo')

# print(match_obj.group())

# search_obj=re_obj.search('This is my foo foo')
# print(search_obj.group())
re_obj=re.compile(r'(ab)cd(?P<name>ef)')
search_obj=re_obj.search('hi.abcdefgei')
#正则表达式对象
print(search_obj.re)
#目标字符串开始位置
print(search_obj.pos)
#位置字符串位置的结束位置后一位
print(search_obj.endpos)
#最后一组组名
print(search_obj.lastgroup)
#最后一组是第几组
print(search_obj.lastindex)
print('---------------------')
#得到匹配字符串在目标字符串起始位置
print(search_obj.start())
#得到匹配字符串在目标字符串结束位置下一个
print(search_obj.end())
#得到匹配字符串在目标字符串开始和结束位置位置
print(search_obj.span())
#默认参数为0即获取整个正则表达式匹配内容
print(search_obj.group())
print(search_obj.group(1))
print(search_obj.group(2))
#返回全部子组内容，以一个元组形式返回
print(search_obj.groups())
#获取所有组名，键值关系，值
print(search_obj.groupdict())