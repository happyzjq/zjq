import pymysql
import random


bankname = "中国工商银行昌平支行"

#数据库连接函数
def mysqlcon():
    # 连接数据库
    conn = pymysql.connect(
        host="localhost",  #主机的名或主机IP地址
        user="root",       #MySQL的用户
        password="123456", #MySQL用户的密码
        database="bank"    #连接的数据库
    )
    return  conn
#获取银行的数据库
def bank():

    #连接数据库
    connect = mysqlcon()

    #创建控制台
    cursor =connect.cursor()

    #查询银行的用户表SQL语句
    sql = "select * from user"

    #执行查询SQL语句
    cursor.execute(sql)

    #提交执行命令
    connect.commit()

    #提取银行用户表数据
    date = cursor.fetchall()

    #关闭控制台资源
    cursor.close()
    #关闭数据库连接资源
    connect.close()
    return date

#根据用户账号查询银行用户数据
def select_bank(account):
    # 连接数据库
    connect = mysqlcon()

    # 创建控制台
    cursor = connect.cursor()

    # 查询银行的用户表SQL语句
    sql = "select * from user where  account=%s"

    param=[account]

    # 执行查询SQL语句
    cursor.execute(sql,param)

    # 提交执行命令
    connect.commit()
    # 提取银行用户表数据
    date = cursor.fetchall()
    # 关闭控制台资源
    cursor.close()
    # 关闭数据库连接资源
    connect.close()
    return  date

#根据用户名查询用户的数据
def select1_bank(username):
    # 连接数据库
    connect = mysqlcon()

    # 创建控制台
    cursor = connect.cursor()

    # 查询银行的用户表SQL语句
    sql = "select * from user where  username=%s"

    # 执行查询SQL语句
    cursor.execute(sql, username)

    # 提交执行命令
    connect.commit()
    # 提取银行用户表数据
    date = cursor.fetchall()
    return date

#根据用户账号与密码更新用户的存额  存钱
def update_addmoney(money,account):
    # 连接数据库
    connect = mysqlcon()

    # 创建控制台
    cursor = connect.cursor()

    # 查询银行的用户表SQL语句
    sql = "update user set money=money+%s where account=%s"

    param = [money,account]

    # 执行查询SQL语句
    cursor.execute(sql, param)

    # 提交执行命令
    connect.commit()

    # 关闭控制台资源
    cursor.close()
    # 关闭数据库连接资源
    connect.close()

#根据用户账号与密码更新用户的存额  取钱
def update_drawmoney(money,account, password):
    # 连接数据库
    connect = mysqlcon()

    # 创建控制台
    cursor = connect.cursor()

    # 查询银行的用户表SQL语句
    sql = "update user set money=money-%s where account=%s and password=%s"

    param = [money,account, password]

    # 执行查询SQL语句
    cursor.execute(sql, param)

    # 提交执行命令
    connect.commit()

    # 关闭控制台资源
    cursor.close()
    # 关闭数据库连接资源
    connect.close()


#插入数据到银行用户表
def insert_bank(account, username, password, country, province, street, door, money,  bankname):
    # 连接数据库
    connect = mysqlcon()
    # 创建控制台
    cursor = connect.cursor()

    # 插入用户数据的SQL语句
    sql = "insert into user(account, username, password, country, province, street, door, money, bankname) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account, username, password, country, province, street, door, money, bankname]
    # 执行查询SQL语句
    cursor.execute(sql, param)

    # 提交执行命令
    connect.commit()

    # 关闭控制台资源
    cursor.close()
    # 关闭数据库连接资源
    connect.close()

def welcome():
    print("---------------------------------------")
    print("-     中国工商银行账户管理系统V1.0      -")
    print("---------------------------------------")
    print("-  1.开户                             -")
    print("-  2.存钱                             -")
    print("-  3.取钱                             -")
    print("-  4.转账                             -")
    print("-  5.查询                             -")
    print("-  6.Bye!                             -")
    print("--------------------------------------")

#工商银行开户逻辑
def bank_addUser(account,username,password,country,province,street,door,money):
    #获取银行的用户数据表
    banks = bank()
    user = select1_bank(username)
    if len(banks) > 100:
        return 3
    #判断 user是不是一个空元组（）   是空元组执行数据插入  不是空元组返回2
    if not user:
        insert_bank(account, username, password, country, province, street, door, money, bankname)
        return 1
    else:
        return 2
#开户的数据输入
def addUser():

    username = input("请输入姓名：")

    password = input("请输入密码：")

    country = input("请输入国籍：")

    province = input("请输入省份：")

    street = input("请输入街道：")

    door = input("请输入您家门牌号：")

    money =int(input("请输入初始化您的银行卡余额："))

    # datetime = input("请输入开户日期：")

    account = random.randint(10000000, 99999999)

    status = bank_addUser(account,username,password,country,province,street,door,money)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        data = select1_bank(username)
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%d
            密码：%s
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户时间：%s
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (data[0][1],data[0][0],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9]))


# 银行转账逻辑
def bank_outaccin(outacc, inacc, outpassword, outmoney):
    # 根据输入的转出账号获取数据库里转出账号数据数据，没有该账号返回一个空元组（）
    outdata = select_bank(outacc)
    #根据输入的转入账号获取数据库里转入账号数据数据，没有该账号返回一个空元组（）
    indata = select_bank(inacc)

    #判断 outdata是不是一个空元组（）   是空元组返回 1
    if not outdata:
        print("转出账号不存在！")
        return 1
    #判断 indata是不是一个空元组（）   是空元组返回1
    elif not indata:
        print("转入账号不存在！")
        return 1
    else:
        if outpassword != outdata[0][2]:
            return 2
        elif outmoney > outdata[0][7]:
            return 3
        else:
            # 连接数据库
            connect = mysqlcon()
            # 创建控制台
            cursor = connect.cursor()

            # 插入用户数据的SQL语句
            # 更新转入账户的余额
            sql = "update user set money=money+%s where account=%s"
            # 更新转出账户的余额
            sql1 = "update user set money=money-%s where account=%s"
            # #根据用户账号查询用户账号和密码
            # sql2 = "select account,password from user where account=%s"

            # sql3 = "select account,passwprd from user where account=%s and password=%s"

            param = [outmoney, inacc]

            param1 = [outmoney, outacc]
            # 执行查询SQL语句
            cursor.execute(sql, param)
            cursor.execute(sql1, param1)

            # 提交执行命令
            connect.commit()

            # 关闭控制台资源
            cursor.close()
            # 关闭数据库连接资源
            connect.close()
            return 4


# 转账的输入数据
def outaccin():
    outacc = int(input("请输出转出的账号："))

    inacc = int(input("请输入转入的账号："))

    outpassword = input("转出账号的密码：")

    outmoney = int(input("请输入转出的金额："))

    status = bank_outaccin(outacc, inacc, outpassword, outmoney)

    if status == 1:
        print("请确定账号后，重新输入账号")
    elif status == 2:
        print("密码不正确！")
    elif status == 3:
        print("转出账户金额不足，无法转账！")
    elif status == 4:
        print("转账成功！")

# 存钱逻辑
def bank_inmoney(inaccuser,inaccmoney):
    #根据输入的账号获取数据库该账号的所有的数据，没有改账号返回一个空元组（）
    data = select_bank(inaccuser)
    #判断 data是不是一个空元组（）   是空元组返回False  不是执行update_addmoney函数进行存钱操作
    if not data:
        print("该账号不存在！")
        return False
    else:
        update_addmoney(inaccmoney,inaccuser)
        print("存钱成功！")







#存钱输入数据
def inmoney():

    inaccuser = int(input("请输入用户的账号："))

    inaccmoney = int(input("请输入存去的金额："))

    status = bank_inmoney(inaccuser,inaccmoney)

    status == False




# 取钱逻辑
def bank_outmoney(outaccuser,outpassword,outusermoney):
    # 根据输入的账号获取数据库该账号的所有的数据，没有改账号返回一个空元组（）
    data = select_bank(outaccuser)
    # 判断 data是不是一个空元组（）   是空元组返回1
    if not data:
        return 1
    else:
        if outpassword != data[0][2]:
            return 2
        elif outusermoney > data[0][7]:
            return 3
        else:
            update_drawmoney(outusermoney,outaccuser,outpassword)
            print("取钱成功！")





#取钱输入数据
def outmoney():
    outaccuser = int(input("请输入用户的账号："))

    outpassword = input("请输入用户的密码：")

    outusermoney = int(input("请输入取钱金额："))

    status = bank_outmoney(outaccuser,outpassword,outusermoney)

    if status == 1:
        print("该用户不存在！")
    if status == 2:
        print("密码不正确！")
    if status == 3:
        print("账户余额不足！")


# 查询逻辑
def bank_insert(insertuser,insertuserpwd):
    # 根据输入的账号获取数据库该账号的所有的数据，没有改账号返回一个空元组（）
    data = select_bank(insertuser)

    if not data:
        print("该用户不存在！")
        return None
    else:
        if insertuserpwd != data[0][2]:
            print("密码不正确！")
            return None
        else:
            print("-------------查询的账号信息如下------------")
            print("用户名：", data[0][1])
            print("账号：", data[0][0])
            print("密码：", data[0][2])
            print("国籍：", data[0][3])
            print("省份：", data[0][4])
            print("街道：", data[0][5])
            print("门牌号：", data[0][6])
            print("余额：", data[0][7])
            print("开户日期：", data[0][8])
            print("开户银行：", data[0][9])



# 查询输入数据
def insertacc():
    insertuser = int(input("请输入用户账号："))

    insertuserpwd = input("请输入账号密码：")

    status = bank_insert(insertuser,insertuserpwd)

    status == None

while True:
    welcome()
    chose = input("请输入业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        inmoney()
    elif chose == "3":
        outmoney()
    elif chose == "4":
        outaccin()
    elif chose == "5":
        insertacc()
    elif chose == "6":
        print("欢迎下次光临！！！")
        break



