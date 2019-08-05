
def menu():
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
|)q退出                      |                    
|)9保存信息到is.txt         |　　　　　　　　
|)10从is.txt提取数据         |
|)11能保存到excel文件(si.csv)|
|)12从excel文件中提取数据(si.csv)|        
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
def info_9():
    f=open('si.txt','w')
    l2=str(l)
    s=f.writelines(l2)
    f.close()

def info_10():
    f=open('si.txt','r')
    s=f.read()
    f.close()
    return s
def info_11():
    f=open('si.csv','wb')
    for d in l:
        s="%s,%d,%d\r\n"%(d['name'],d['age'],d['score'])
        s1=s.encode('utf-8')
        f.write(s1)
    f.close()
def info_12():
    f=open('si.csv','rb')
    s=f.read()
    s2=s.decode('utf-8')
    print(s2)
    f.close()

l=[]
while True:
    menu()
    x=input('请输入选项：')
    if x=='1':
        info_1()
    elif x=='2':
        info_2()
    elif x=='3':
        info_3()
    elif x=='4':
        info_4()
    elif x=='5':
        l=info_5()
        info_2()
    elif x=='6':
        l=info_6()
        info_2()
    elif x=='7':
        l=info_7()
        info_2()
    elif x=='8':
        l=info_8()
        info_2()
    elif x=='q':
        break
    elif x=='9':
        info_9()
    elif x=='10':
        info_10()
    elif x=='11':
        info_11()
    elif x=='12':
        info_12()    
    else:
        print('输入错误，请重新输入：')
