
def zhujiemian():
    print("""
+----------------------------+
|)1添加学生信息              |              
|)2显示所有学生信息          |           
|)3删除学生信息              |　　　　　　　　　　　　　　
|)4修改学生成绩　            |　　　　　　　　　　　　
|)5按学生成绩高到低显示信息  |　　　　　
|)6按学生成绩低到高显示信息  |　　　　
|)7按学生年龄高到低显示信息  |    
|)8按学生年龄低到高显示信息  |    
|)9退出                      |                    
|)10保存信息到is.txt         |　　　　　　　　
|)11从is.txt提取数据         |        
+----------------------------+""" )
        
def info_1():
    while True:
        x=input('请输入学生姓名：')
        if x=='':
            break
        y=int(input('请输入学生年龄：'))
        z=int(input('请输入学生成绩：'))  
        d={'name':x,'age':y,'score':z}
        l.append(d)
    return l
def info_2():
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
def info_3():
    x=str(input('请输入要删除学生信息的姓名：'))
    i=0
    for d in l:
        if d['name']==x:
            del l[i]
        i+=1
def info_4():
    x=str(input('请输入要修改成绩的学生姓名：'))
    y=int(input('请输入新的成绩：'))
    for d in l:
        if d['name']==x:
            d['score']=y
def info_5():
    def score_1(d):
        return d['score']
    l2=sorted(l,key=score_1,reverse=True)
    return l2
def info_6():
    def score_1(d):
        return d['score']
    l2=sorted(l,key=score_1,reverse=False)
    return l2
def info_7():
    def age_1(d):
        return d['age']
    l2=sorted(l,key=age_1,reverse=True)
    return l2
def info_8():
    def age_1(d):
        return d['age']
    l2=sorted(l,key=age_1,reverse=False)
    return l2
def info_10():
    f=open('./si.txt','a')
    l2=str(l)
    s=f.writelines(l2)
    f.close()

def info_11():
    f=open('./si.txt','r')
    s=f.readline()
    f.close()
    return s