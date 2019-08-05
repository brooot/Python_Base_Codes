# 1.1输入任意５个学生的姓名，年龄，成绩，学生信息，存入字典，
# 然后把学生的信息字典放入列表中，每个学生的信息需要手动输入，内部存储格式如下：
# [{'name':'tarena','age',:20,'score':99},{'name':'xiaowang',
# 'age',:21,'score':59　　　　},....]
# )1.打印所有学生信息如下：
# +-------------+-------------+--------------+
# |     姓名　　　　 |   年龄　　　　　　|     成绩　　　  　|
# +-------------+-------------+--------------+
# |    张         |　　　　　　　　　　　　　|            |
# |               |             |            |
# +---------------+-------------+------------+
def mylist():
    l=[]
    for i in range(3):
        no=str(i+1)
        x=input('请输入'+no+'学生姓名：')
        y=int(input('请输入'+no+'学生年龄：'))
        z=int(input('请输入'+no+'学生成绩：'))  
        d={'name':x,'age':y,'score':z}
        l.append(d)
    return l
l=mylist()

def myline3(l):
    line1='+-------------+-------------+-------------+'
    line2='+    name     +     age     +    score    +'
    print(line1)
    print(line2)
    print(line1)
    for d in l:
        print('|'+d['name'].center(13)+
               '|'+str(d['age']).center(13)+
               '|'+str(d['score']).center(13)+'|')
    print(line1)
myline3(l)

# 1.2输入学生的分数线，把高于这个分数的学生信息打印出来，如输入：９０打印如下

# scoreline=int(input('请输入分数线：'))
# l2=[x for x in l if x['score']>scoreline]
# myline3(l2)

 # ）１．按成绩从高到低打印信息
 # ）２．按年龄从高到低打印信息
 # ）３．按年龄从低到高打印信息
 # ）４．按原来输入的顺序打印信息
def score1(d):
    return d['score']
l3=sorted(l,key=score1,reverse=True) 
myline3(l3)

def age1(d):
    return d['age']
l4=sorted(l,key=age1)
myline3(l4)
l5=sorted(l,key=age1,reverse=True)
myline3(l5)