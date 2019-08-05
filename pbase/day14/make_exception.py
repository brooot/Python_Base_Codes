def get_score():
    score=int(input('请输入成绩：:'))
    assert 0<=score<=100,'成绩超出范围哦'
    return score
score=get_score()
print('学生成绩为：',score)

# try:
#     print(get_score())
# except ValueError:
#     print('值错误')
# print('game over')


