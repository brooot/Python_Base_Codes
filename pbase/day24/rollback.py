import pymysql
db=pymysql.connect("localhost","root","123456","python")
cur=db.cursor()
sql_insert1="insert into t1 values(6,'dehua.liu',50,'boy');"
sql_insert2="update t1 set age=88 where id=5;"
try:
    cur.execute(sql_insert1)
    cur.execute(sql_insert2)
    db.commit()
    print("对的")
except:
    print("***")
    db.rollback()




cur.close()
db.close()