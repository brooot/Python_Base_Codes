import pymysql
db=pymysql.connect("localhost","root","123456","python")
cur=db.cursor()
cur.execute("insert into t1 values(1,'sanfeng.zhang',30,'boy'),\
    (2,'wuji.zhang',25,'boy'),\
    (3,'jinlian.pan',20,'girl'),\
    (4,'menqing.xi',40,'boy'),\
    (5,'dalang.wu',33,'boy');")
cur.execute("select * from t1;")
data=cur.fetchone()
print("fetchone的结果是:",data)
db.commit()
cur.close()
db.close()
