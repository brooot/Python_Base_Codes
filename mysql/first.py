import pymysql

#1、创建与数据库连接对象
db = pymysql.connect(host="localhost",user="root",
                password="xzl1122",database="db3",
                charset="utf8")

#2、利用db方法创建游标对象
cur = db.cursor()

#3、利用游标对象的 execute()方法执行SQL命令
try:
    sql_select = "select * from sheng"
    cur.execute(sql_select)
    data1 = cur.fetchall()
    for i in data1:
        print(i)
    #db.commit()
except Exception as e:
    db.rollback()
    print("出现错误，已回滚。\n错误内容为：" + e)
#4、提交到数据库执行
db.commit()

#5、关闭游标对象
cur.close()

#6、断开数据库连接
db.close()