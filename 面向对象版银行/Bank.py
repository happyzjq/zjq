import random
from Utils import Utils
from DBUtils import update
from DBUtils import select



class Bank():

    bank = {}  # 银行数据库

    __bank_name = "中国工商银行昌平支行"  # 银行名称

    bank_choose = {"1": "开户", "2": "存钱", "3": "取钱", "4": "转账", "5": "查询", "6": "Bye!"}  # 银行业务选项

    # 银行的名称是建立时就定下来的，不存在用户来设置其名称
    # __bank_name=None
    def getBankName(self):
        return self.__bank_name

    # 判断是否在某个范围之内
    def isExists(self,chose, data):
        if chose in data:
            return True
        return False

    # 银行开户逻辑
    def bank_addUser(self,username, password, country, province, street, door,
                     money):

        # 查询银行的表中的用户数量
        sql = "select count(*) from user"
        param = []
        sum = select(sql, param, mode="all")

        if sum[0][0] > 100:
            return 3

        # 根据username查询数据库中是否存在该用户
        sql1 = "select username from user where username=%s"
        param1 = [username]
        user = select(sql1, param1, mode="all")

        if not user:
            sql3 = "insert into user(account, username, password, country, province, street, door, money, bankname) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param3 = [Utils().getRandom(), username, password, country, province, street, door, money, self.__bank_name]
            update(sql3, param3)
            return 1
        else:
            return 2

    # 银行存钱逻辑
    def bank_inmoney(self,inaccuser, inaccmoney):
        # 根据输入的账号获取数据库该账号的所有的数据，没有改账号返回一个空元组（）
        sql = "select * from user where account=%s"
        param = [inaccuser]
        data = select(sql, param, mode="all")
        # 判断 data是不是一个空元组（）   是空元组返回False  不是执行update_addmoney函数进行存钱操作
        if not data:
            print("该账号不存在！")
            return False
        else:
            sql1 = "update user set money=money+%s where account=%s"
            param1 = [inaccmoney, inaccuser]
            update(sql1, param1)
            print("存钱成功！")

    # 取钱逻辑
    def bank_outmoney(self,outaccuser, outpassword, outusermoney):
        # 根据输入的账号获取数据库该账号的所有的数据，没有改账号返回一个空元组（）
        sql = "select * from user where account=%s"
        param = [outaccuser]
        data = select(sql, param, mode="all")
        # 判断 data是不是一个空元组（）   是空元组返回1
        if not data:
            return 1
        else:
            if outpassword != data[0][2]:
                return 2
            elif outusermoney > data[0][7]:
                return 3
            else:
                sql1 = "update user set money=money-%s where account=%s and password=%s"
                param1 = [outusermoney, outaccuser, outpassword]
                update(sql1, param1)
                print("取钱成功！")
    # 银行转账逻辑
    def bank_outaccin(self,outacc, inacc, outpassword, outmoney):
        # 根据输入的转出账号获取数据库里转出账号数据数据，没有该账号返回一个空元组（）
        sql = "select * from user where account=%s"
        param = [outacc]
        outdata = select(sql, param, mode="all")
        # 根据输入的转入账号获取数据库里转入账号数据数据，没有该账号返回一个空元组（）
        param1 = [inacc]
        indata = select(sql, param1, mode="all")

        # 判断 outdata是不是一个空元组（）   是空元组返回 1
        if not outdata:
            print("转出账号不存在！")
            return 1
        # 判断 indata是不是一个空元组（）   是空元组返回1
        elif not indata:
            print("转入账号不存在！")
            return 1
        else:
            if outpassword != outdata[0][2]:
                return 2
            elif outmoney > outdata[0][7]:
                return 3
            else:
                # 更新转入账户的余额
                sql1 = "update user set money=money+%s where account=%s"
                param3 = [outmoney, inacc]
                # 更新转出账户的余额
                sql2 = "update user set money=money-%s where account=%s"
                param4 = [outmoney, outacc]
                update(sql1, param3)
                update(sql2, param4)
                return 4

    #查询逻辑
    def bank_insert(self,insertuser, insertuserpwd):
        # 根据输入的账号获取数据库该账号的所有的数据，没有改账号返回一个空元组（）
        sql = "select * from user where account=%s"
        param = [insertuser]
        data = select(sql, param, mode="all")

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

