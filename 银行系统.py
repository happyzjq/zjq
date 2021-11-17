import random

# 银行的数据库
bank = {}
# 银行名称
bank_name = "中国工商银行昌平支行"


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


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, door, money):
    if len(bank) > 100:
        return 3

    if username in bank:
        return 2

    # 正常开户
    bank[username] = {
        "account": account,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": money,
        "bank_name": bank_name
    }
    return 1


# 开户的输入数据
def addUser():
    username = input("请输入姓名：")

    password = input("请输入密码：")

    country = input("请输入国籍：")

    province = input("请输入省份：")

    street = input("请输入街道：")
    door = input("请输入您家门牌号：")

    money = int(input("请输入初始化您的银行卡余额："))

    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, username, password, country, province, street, door, money)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%s
            密码：%s
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (username, account, password, country, province, street, door, money, bank_name))
        print(bank)


# 银行转账逻辑
def bank_outaccin(outacc, inacc, outpassword, outmoney):
    for k,v in bank.items():
        # print(v["account"])
        # print(type(v["account"]))
        # print(outacc)
        # print(type(outacc))
        if outacc != v["account"] and inacc != v["account"]:
            return 1
        # else:
        #     print("该用户存在")
        if outacc == bank[k]["account"]:
            if outpassword != bank[k]["password"]:
                return 2
            # else:
            #     print("密码正确")
            if outmoney > bank[k]["money"]:
                print(bank[k]["money"])
                return 3
            # else:
            #     print("金额足够!")
            else:
                bank[k]["money"] = bank[k]["money"] - outmoney

        if inacc == bank[k]["account"]:
            bank[k]["money"] = bank[k]["money"] + outmoney
            return 4







# 转账的输入数据
def outaccin():
    outacc = int(input("请输出转出的账号："))

    inacc = int(input("请输入转入的账号："))

    outpassword = input("转出账号的密码：")

    outmoney = int(input("请输入转出的金额："))

    status = bank_outaccin(outacc, inacc, outpassword, outmoney)

    if status == 1:
        print("该用户不存在")
    elif status == 2:
        print("密码不正确！")
    elif status == 3:
        print("转出账户金额不足，无法转账！")
    elif status == 4:
        print("转账成功！")
        # print(bank)

# 存钱逻辑
def bank_inmoney(inaccuser,inaccmoney):
    for k in bank.keys():
        if inaccuser != bank[k]["account"]:
            return False
        else:
            bank[k]["money"] = bank[k]["money"] +inaccmoney
            print("存钱成功！")

#存钱输入数据
def inmoney():
   inaccuser = int(input("请输入用户的账号："))

   inaccmoney = int(input("请输入存去的金额："))

   status = bank_inmoney(inaccuser,inaccmoney)

   if status == False:
       print("该用户不存在！")
# 取钱逻辑
def bank_outmoney(outaccuser,outpassword,outusermoney):
    for k in bank.keys():
        if outaccuser != bank[k]["account"]:
            return 1
        if outaccuser == bank[k]["account"]:
            if outpassword != bank[k]["password"]:
                return 2
            if outusermoney > bank[k]["money"]:
                return 3
            else:
                bank[k]["money"] = bank[k]["money"] - outusermoney
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
    for k in bank.keys():
        if insertuser != bank[k]["account"]:
            print("该用户不存在")
            return None
        if insertuser == bank[k]["account"]:
            if insertuserpwd != bank[k]["password"]:
                print("密码不正确！")
                return None
            else:
                print("-------------查询的账号信息如下------------")
                print("用户名：",k)
                print("账号：",bank[k]["account"])
                print("密码：",bank[k]["password"])
                print("国籍：",bank[k]["country"])
                print("省份：",bank[k]["province"])
                print("街道：",bank[k]["street"])
                print("门牌号：",bank[k]["door"])
                print("余额：",bank[k]["money"])
                print("开户银行：",bank[k]["bank_name"])



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
