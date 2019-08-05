import pymysql
db=pymysql.connect("localhost","root","123456","python")
cur=db.cursor()

sql_select="select * from t1;"
cur.execute(sql_select)

firstrow=cur.fetchone()
print("第一条记录是:",firstrow)
print("++++++++++++++++++++++")

manysize= cur.fetchmany(2)
print("fetchmany(2)的记录是:",manysize)
print("++++++++++++++++++++++")

allrow=cur.fetchall()
print("fetchall的记录是:",allrow)
print("++++++++++++++++++++++")



db.commit()
cur.close()
db.close()