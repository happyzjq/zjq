from DBUtils import update
from DBUtils import select
import random

#工商银行开户逻辑为父类
class fbank_addUser:
    __bankname = "中国工商银行昌平支行"
    def bank_addUser(self,account,username,password,country,province,street,door,money):

        #查询银行的表中的用户数量
        sql = "select count(*) from user"
        param =[]
        sum = select(sql,param,mode="all")

        if sum[0][0] > 100:
            return 3

        #根据username查询数据库中是否存在该用户
        sql1 ="select username from user where username=%s"
        param1 = [username]
        user = select(sql1,param1,mode="all")

        if not user:
            sql3 = "insert into user(account, username, password, country, province, street, door, money, bankname) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param3 = [account, username, password, country, province, street, door, money, self.__bankname]
            update(sql3,param3)
            return 1
        else:
            return 2


#开户的数据输入为子类
class faddUser(fbank_addUser):
    def addUser(self):

        username = input("请输入姓名：")

        password = input("请输入密码：")

        country = input("请输入国籍：")

        province = input("请输入省份：")

        street = input("请输入街道：")

        door = input("请输入您家门牌号：")

        money =int(input("请输入初始化您的银行卡余额："))

        # datetime = input("请输入开户日期：")

        account = random.randint(10000000, 99999999)

        status = super().bank_addUser(account,username,password,country,province,street,door,money)

        if status == 3:
            print("对不起，该银行用户已满，请携带证件到其他银行办理！")
        elif status == 2:
            print("您之前已经开过户！禁止重复开户！")
        elif status == 1:
            print("嘻嘻，开户成功！以下卡户的个人信息：")
            sql = "select * from user where username=%s"
            param = [username]
            data = select(sql,param,mode="all")
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
            print(info % (
            data[0][1], data[0][0], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6], data[0][7], data[0][8],
            data[0][9]))


# 银行转账逻辑为父类
class fbank_outaccin:
    def bank_outaccin(self,outacc, inacc, outpassword, outmoney):
        # 根据输入的转出账号获取数据库里转出账号数据数据，没有该账号返回一个空元组（）
        sql = "select * from user where account=%s"
        param = [outacc]
        outdata = select(sql,param,mode="all")
        #根据输入的转入账号获取数据库里转入账号数据数据，没有该账号返回一个空元组（）
        param1 = [inacc]
        indata = select(sql,param1,mode="all")

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
                # 更新转入账户的余额
                sql1 = "update user set money=money+%s where account=%s"
                param3 = [outmoney,inacc]
                # 更新转出账户的余额
                sql2 = "update user set money=money-%s where account=%s"
                param4 = [outmoney,outacc]
                update(sql1,param3)
                update(sql2,param4)
                return 4


# 转账的输入数据为子类
class foutaccin(fbank_outaccin):
    def outaccin(self):
        outacc = int(input("请输出转出的账号："))

        inacc = int(input("请输入转入的账号："))

        outpassword = input("转出账号的密码：")

        outmoney = int(input("请输入转出的金额："))

        status = super().bank_outaccin(outacc, inacc, outpassword, outmoney)

        if status == 1:
            print("请确定账号后，重新输入账号")
        elif status == 2:
            print("密码不正确！")
        elif status == 3:
            print("转出账户金额不足，无法转账！")
        elif status == 4:
            print("转账成功！")

# 存钱逻辑为父类
class fbank_inmoney:
    def bank_inmoney(self,inaccuser,inaccmoney):
        #根据输入的账号获取数据库该账号的所有的数据，没有改账号返回一个空元组（）
        sql = "select * from user where account=%s"
        param = [inaccuser]
        data = select(sql,param,mode="all")
        #判断 data是不是一个空元组（）   是空元组返回False  不是执行update_addmoney函数进行存钱操作
        if not data:
            print("该账号不存在！")
            return False
        else:
            sql1 = "update user set money=money+%s where account=%s"
            param1 = [inaccmoney,inaccuser]
            update(sql1,param1)
            print("存钱成功！")

#存钱输入数据为子类
class finmoney(fbank_inmoney):
    def inmoney(self):

        inaccuser = int(input("请输入用户的账号："))

        inaccmoney = int(input("请输入存去的金额："))

        status = super().bank_inmoney(inaccuser,inaccmoney)

        status == False




# 取钱逻辑为父类
class fbank_outmoney:
    def bank_outmoney(self,outaccuser,outpassword,outusermoney):
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
                param1 = [outusermoney,outaccuser,outpassword]
                update(sql1, param1)
                print("取钱成功！")


#取钱输入数据为子类
class foutmoney(fbank_outmoney):
    def outmoney(self):
        outaccuser = int(input("请输入用户的账号："))

        outpassword = input("请输入用户的密码：")

        outusermoney = int(input("请输入取钱金额："))

        status = super().bank_outmoney(outaccuser,outpassword,outusermoney)

        if status == 1:
            print("该用户不存在！")
        if status == 2:
            print("密码不正确！")
        if status == 3:
            print("账户余额不足！")

# 查询逻辑为父类
class fbank_insert:
    def bank_insert(self,insertuser,insertuserpwd):
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



# 查询输入数据为子类
class finsertacc(fbank_insert):
    def insertacc(self):
        insertuser = int(input("请输入用户账号："))

        insertuserpwd = input("请输入账号密码：")

        status = super().bank_insert(insertuser,insertuserpwd)

        status == None


#欢迎界面未父类
class fwelcome:
    def welcome(self):
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
#while为子类
class fwhile(fwelcome):
    def wwhile(self):
        while True:
            super().welcome()
            chose = input("请输入业务编号：")
            if chose == "1":
                a = faddUser()
                a.addUser()
            elif chose == "2":
                a = finmoney()
                a.inmoney()
            elif chose == "3":
                a = foutmoney()
                a.outmoney()
            elif chose == "4":
                a = foutaccin()
                a.outaccin()
            elif chose == "5":
                a = finsertacc()
                a.insertacc()
            elif chose == "6":
                print("欢迎下次光临！！！")
                break


fwhile().wwhile()



