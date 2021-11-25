import pymysql
import xlrd
from DBUtils import select

host = "localhost"  # 主机的名或主机IP地址
user = "root"  # MySQL的用户
password = "123456"  # MySQL用户的密码
database = "bank"  # 连接的数据库

wb = xlrd.open_workbook(filename="百度合作单位-人员管理-二期.xls")
tables = wb.sheet_by_index(0)

nows = tables.nrows

param = []
b =()
# for i in range(1, nows):
#     data = tables.row_values(i)
#     b = tuple(data)
#     # print(type(b))
#     param.append(b)
# print(param)
#批量插入数据到数据库
def insert_baidu():
    for i in range(1,nows):
        data = tables.row_values(i)
        b = tuple(data)
        # print(type(b))
        param.append(b)

    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    sql = "insert into baiduuser value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

    try:
        cursor.executemany(sql,param)
        con.commit()
    except Exception as e:
        con.rollback()
    cursor.close()
    con.close()

insert_baidu()

# a)统计所有表格中有多少人
def count_people():
    sql = "SELECT COUNT(*) FROM baiduuser"
    param = []

    sumpeople = select(sql,param,mode="one")
    print("--------------------------------")
    print("表格中共有%s人" % sumpeople[0])
    print("--------------------------------")

count_people()

# b)统计办电信，联通，移动的用户数量（14,17开头为电信）（13开头为移动）（15开头为联通）
def phone():
    sql = "SELECT COUNT(*) FROM baiduuser WHERE (电话号码) LIKE %s OR (电话号码) LIKE %s"
    sql1 = "SELECT COUNT(*) FROM baiduuser WHERE (电话号码) LIKE %s"
    sql2 = "SELECT COUNT(*) FROM baiduuser WHERE (电话号码) LIKE %s"
    param = ['14%','17%']
    param1 = ['13%']
    param2 = ['15%']
    #移动
    mobilephone = select(sql1,param1,mode="one")
    #电信
    telecomnumber = select(sql,param,mode="one")
    #联通
    unicomnumber = select(sql2,param2,mode="one")
    print("--------------------------------")
    print("电信的用户数量：%s人" % telecomnumber[0])
    print("移动的用户数量：%s人" % mobilephone[0])
    print("联通的用户数量：%s人" % unicomnumber[0])
    print("--------------------------------")

phone()


# c)总公司男女人数
def gender():
    sql = "SELECT COUNT(*) FROM baiduuser WHERE 性别='男'"
    sql2 = "SELECT COUNT(*) FROM baiduuser WHERE 性别='女'"
    param = []
    boynum = select(sql,param,mode="one")
    girlnum = select(sql2,param,mode="one")
    print("--------------------------------")
    print("公司的男士人数为：%s人" % boynum[0])
    print("公司的女士人数为：%s人" % girlnum[0])
    print("--------------------------------")

gender()

# d)年龄超过45岁的老员工人数
def oldpeople():
    sql = "SELECT COUNT(*) FROM baiduuser WHERE 年龄>45"
    param = []
    oldpeo = select(sql,param,mode="one")
    print("--------------------------------")
    print("年龄超过45岁的老员工人数为：%s人" % oldpeo[0])
    print("--------------------------------")

oldpeople()
# e)薪资高于8000元的高薪人员数量和薪资低于3000的底薪人员数量
def salary():
    sql = "SELECT COUNT(*) FROM baiduuser WHERE 薪资<3000"
    sql1 = "SELECT COUNT(*) FROM baiduuser WHERE 薪资>8000"
    param = []
    lowsalary = select(sql,param,mode="one")
    highsalary = select(sql1,param,mode="one")
    print("--------------------------------")
    print("薪资低于3000的底薪人员数量:%s人" % lowsalary[0])
    print("薪资高于8000元的高薪人员数量:%s人" % highsalary[0])
    print("--------------------------------")

salary()

# f)统计去传媒公司的工作的人员数量
def media():
    sql = "SELECT COUNT(*) FROM baiduuser WHERE 外包公司 LIKE %s"
    param = ['%传媒%']
    medianum = select(sql,param,mode="one")
    print("--------------------------------")
    print("去传媒公司的工作的人员数量:%s人" % medianum[0])
    print("--------------------------------")

media()
# g)统计一下可能在疫情高危地区的人数（高危地区：黑龙江，北京，福建，四川）
def highriskarea():
    sql = "SELECT COUNT(*) FROM baiduuser WHERE 居住地址 LIKE %s OR 居住地址 LIKE %s OR 居住地址 LIKE %s OR 居住地址 LIKE %s"
    param = ['%黑龙江%','%福建%','%北京%','%四川%']

    hingarea = select(sql,param,mode="one")

    print("--------------------------------")
    print("可能在疫情高危地区的人数（高危地区：黑龙江，北京，福建，四川）:%s人" % hingarea[0])
    print("--------------------------------")

highriskarea()


# b = tables.row_values(1)
# print(b[1])
# print(type(b[1]))
# print(type(int(b[1])))
# print(b[13])
# print(nows)
# def insertbaidu():
#data[1], data[2], data[3], int(data[4]), data[5], data[6], int(data[7]), data[8], data[9], data[10],
  #      int(data[11]), data[12], data[13]
    # con = pymysql.connect(host=host, user=user, password=password, database=database)
    # # cursor = con.cursor()
    # #
    # # param = [data[1], data[2], data[3], int(data[4]), data[5], data[6], int(data[7]), data[8], data[9], data[10],
    # #          int(data[11]), data[12], data[13]]
    # # print(param)
    # #
    # # sql = "insert into baiduuser value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
    # #
    # # cursor.execute(sql, param)
    # # con.commit()
    # # cursor.close()
    # # con.close()

#     a =(data[1], data[2], data[3], int(data[4]), data[5], data[6], int(data[7]), data[8], data[9], data[10],
#              int(data[11]), data[12], data[13])
#     param.append(a)
# # print(param)
# # 连接数据库
# con = pymysql.connect(host=host, user=user, password=password, database=database)
# # 创建控制台
# cursor = con.cursor()
# sql = "insert into baiduuser(身份标识,登录名,真实姓名,密码,电话号码,邮箱,年龄,性别,居住地址,入职日期,薪资,职责,外包公司) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
#
# # cursor.executemany(sql, param)
# # cursor.close()
# # con.commit()
# #
# # con.close()
# try:
#     # 执行SQL语句
#     cursor.executemany(sql, param)
# except Exception as e:
#     print("执行MySQL: %s 时出错：%s" % (sql,e))
#     con.rollback()
#     con.close()
#
# # 提交
# con.commit()
# # 关闭资源
# cursor.close()
# con.close()
