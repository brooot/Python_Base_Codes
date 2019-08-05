# 将文件从数据库导出到本地


from pymongo import MongoClient
import gridfs

conn = MongoClient('localhost',27017)
db = conn.grid

# 获取gridfs对象
fs = gridfs.GridFS(db)

# f = open('photo.jpg','rb')

# 得到文件集合对象
files = fs.find()
for file in files:
    # 打印每个文件名称
    print(file.filename)
    if file.filename == 'photo.jpg':
        with open(file.filename,'wb') as f:
            # 从数据库读取内容
            data = file.read()
            # 写入到本地
            f.write(data)


conn.close()