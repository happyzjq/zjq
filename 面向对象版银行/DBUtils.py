import pymysql
host="localhost"  #主机的名或主机IP地址
user="root"       #MySQL的用户
password="123456" #MySQL用户的密码
database="bank"    #连接的数据库

#增 删 改
def update(sql,param):
    # 连接数据库
    con = pymysql.connect(host=host, user=user, password=password, database=database)

    # 创建控制台
    cursor = con.cursor()

    # 执行SQL语句
    cursor.execute(sql, param)
    # 提交
    con.commit()
    # 关闭资源
    cursor.close()
    con.close()


#查
def select(sql,param,mode="many",size=0):
    # 连接数据库
    con = pymysql.connect(host=host, user=user, password=password, database=database)

    # 创建控制台
    cursor = con.cursor()

    #执行SQL语句
    cursor.execute(sql, param)
    #提交
    con.commit()

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return  cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    #关闭资源
    cursor.close()
    con.close()
