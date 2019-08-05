from pymongo import MongoClient
from random import randint

conn = MongoClient('localhost',27017)

db = conn.grade

myset = db.class1

# print("插如前:")
# for i in myset.find({},{'_id':0}):
#     print(i)

cursor = myset.find()
for i in cursor:
    myset.update({'_id':i['_id']},{"$set":{"score" : { "Chinese":randint(80,100), "Math":randint(80,100), "English":randint(80,100) }}})

print("插入后的表为:")
for i in myset.find({},{'_id':0}):
    print(i)

# 按照性别统计人数
p = [
        {'$group':{'_id':"$sex",'count':{'$sum':1}}},
    ]
print("按照性别分组统计人数:")
for i in myset.aggregate(p):
    print(i)

# 统计每名男生的语文成绩:
p = [
        {'$match':{'sex':'w'}},
        {'$project':{'_id':0,'name':1,'score.Chinese':1}}
    ]
print("男生的语文成绩分别为:")
for i in myset.aggregate(p):
    print(i)

# 将女生成绩降序排列
print("将女生成绩降序排列:")
s = [
        {'$match':{'sex':'w'}},
        {'$sort':{'score.English':-1}}
    ]
t = myset.aggregate(s)
for i in t:
    print(i)