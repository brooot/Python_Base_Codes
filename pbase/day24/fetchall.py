import pymysql
db = pymysql.connect("localhost","root","123456")
cur=db.cursor()
useku="use python;"
cur.execute(useku)
sql_select="select * from t1;"
cur.execute(sql_select)
data=cur.fetchmany(3)
# print("fetchmany的结果是:",data)
for i in data:
    print(i)


db.commit()
cur.close()
db.close()