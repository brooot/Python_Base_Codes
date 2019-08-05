# -*- coding: utf-8 -*-  
from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost', 27017)

#创建数据库对象
db = conn.stu

#创建集合对象
# myset = db.class1

# index = myset.ensure_index('name')

# print(index)
# # index = myset.ensure_index([('name',1)])     复合索引


# 获取当前索引
# for i in myset.list_indexes():
#     print(i)

# 删除所有索引
# myset.drop_indexes()

# 删除单个索引
# myset.drop_index('index_name')


# 完整索引创建(复合索引,索引名字,唯一索引,稀疏索引)
# myset.ensure_index([('name',1),('age',-1)],name='MyIndex',unique = True, sparse = True)

# myset.drop_index(index)
# a = myset.list_indexes()
# for i in a:
#     print(i)




# 聚合操作
myset4 = db.class4

p = [
        {'$group':{'_id':'$king',"count":{"$sum":1}}},
        {'$match':{'count':{'$gt':1}}},
    ]

cursor = myset4.aggregate(p)
for i in cursor:
    print(i)




conn.close()