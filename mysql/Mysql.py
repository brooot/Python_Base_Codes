from pymysql import *


class mySql:
    def __init__(self, database,
                 host='localhost',
                 user='root',
                 password='xzl1122',
                 port=3306,
                 charset='utf8'):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset

    def open(self):
        self.db = connect(host=self.host,
                          user=self.user,
                          password=self.password,
                          port=self.port,
                          charset=self.charset,
                          database=self.database)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def getone(self):
        print(self.cur.fetchone()[0])

    def getmany(self, n):
        _data = self.cur.fetchmany(n)
        for _i in _data:
            print(_i[0])
        del _i, _data

    def getall(self):
        _data = self.cur.fetchall()
        for _i in _data:
            print(_i[0])
        del _i, _data

    def show_tables(self):
        self.cur.execute("show tables;")
        print("here are the tables in %s:" % (self.database))
        self.getall()

    def show_databases(self):
        self.cur.execute("show databases;")
        print("here are the databases:")
        self.getall()

    def show_table(self, Table):
        _select = "select * from %s;" % Table
        self.cur.execute(_select)
        self.db.commit()
        _d = self.cur.fetchall()
        print("table %s :" % Table)
        if len(_d):
            for _i in _d:
                print(_i)
            del _i
        else:
            print("empty")
        del _select, _d

    def create_database(self, new_database):
        try:
            _create_database = "create database %s" % new_database
            self.cur.execute(_create_database)
            self.db.commit()
            print("database %s successfully created!" % new_database)
        except Exception as e:
            print("Fail to create database %s." % new_database)
            print(e)
        # self.cur.execute("use %s;"%new_database)

    def use_database(self, selected_database):
        try:
            self.cur.execute("use %s" % selected_database)
            print("database changed to %s successfully!" % selected_database)
        except Exception as e:
            print("Error!\n" + e)

    def show_cur_database(self):
        self.cur.execute("select database();")
        print('current database is:  ', end='')
        self.getall()
        print()
