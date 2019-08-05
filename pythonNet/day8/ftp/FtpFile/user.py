from Mysql import *
from hashlib import sha1
import time

def regist():
    print("欢迎注册！")
    try:
        _name = input("请输入用户名：")
        _passwd = input("请输入密码：")
        s1 = sha1()
        s1.update(_passwd.encode("utf8"))
        encrypted_passwd = str(s1.hexdigest())
        sql.cur.execute("insert into userinfo(username,passwd) values('%s','%s');" % (_name, encrypted_passwd))
        sql.db.commit()
        print('注册成功!')
    except Exception as e:
        print(e)

def login():
    print("欢迎登录！")
    try:
        _name = input("请输入用户名：")
        pwd = get_passwd(_name)
        if not pwd:
            print("抱歉，没有这个用户。")
            return
        inputed_passwd = input("请输入密码：")
        s1 = sha1()
        s1.update(inputed_passwd.encode("utf8"))
        checking_passwd = s1.hexdigest()
        # print(str(pwd),checking_passwd)
        if pwd == checking_passwd:
            print('登录成功！')
            return
        print('密码错误。')
    except Exception as e:
        print(e)


def get_passwd(name):
    sql.cur.execute("select passwd from userinfo where username='%s'" % name)
    sql.db.commit()
    d = sql.cur.fetchone()
    if d:
        return d[0]
    else:
        return None

def menu():
    print("欢迎来到没啥卵用的用户注册与登录系统！")
    print("请选择要进行的操作：")
    print("1:用户注册")
    print("2:用户登录")
    print("3:退出系统")


# def main():
sql = mySql(database='users_database')
sql.open()
# sql.use_database('users_database')
# sql.show_cur_database()
# sql.show_table('userinfo')
while 1:
    try:
        menu()
        operation = int(input("请输入您想要进行的操作编号："))
        if operation == 1:
            regist()
        elif operation == 2:
            login()
        elif operation == 3:
            break
        else:
            print("请输入编号为1-3的整数。")
    except Exception as e:
        print(e)
        print("系统已经退出，下次再来玩哦！")
        break
    finally:    
        time.sleep(1)
        print("\n"*100)

sql.close()
print("系统已经退出，下次再来玩哦！")


# main()