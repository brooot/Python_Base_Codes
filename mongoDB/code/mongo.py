# -*- coding: utf-8 -*-  
from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost', 27017)

#创建数据库对象
db = conn.stu

#创建集合对象
myset = db.class4

# 数据库操作
# print(dir(myset))
# myset.insert({})
# myset.insert_many([{"name":'唐国强','king':'雍正'},{'name':'陈建斌','king':'雍正'}])
# myset.insert_one({})
# myset.save({'_id':1,'name':'聂远','king':'乾隆'})
# myset.save({'_id':1,'name':'吴奇隆','king':'四爷'})

# cursor = myset.find({"name":{'$ne':''}},{'_id':0})
# for i in cursor:
#     print(i)
# print(cursor)


# # next() 方法
myset1 = db.class1
cursor = myset1.find({},{'_id':0})
# print(cursor.next())
# print(cursor.next())


 # 如果使用for 或next() 使 游标位置不在开头的时候调用lilimit skip sort 会报错
# for i in cursor.skip(2).limit(3): 
#     print(i)


# for i in cursor.sort([('age',1),('name',-1)]):
#     print(i)


# 关闭连接
conn.close()