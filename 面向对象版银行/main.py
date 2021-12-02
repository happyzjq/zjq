from Address import  Address
from Bank  import  Bank
from User import  User
from welcome import  Welcome
from Utils import  Utils
from DBUtils import update
from DBUtils import select

# 初始化必要对象
welcome =  Welcome()
utils = Utils()
address = Address()
user = User()
bank = Bank()


# 必要的初始化方法
# 开户方法
def addUser():
    username = utils.inputHelp("用户名")
    password = utils.inputHelp("密码")
    country = utils.inputHelp("居住地址，1.国家：")
    province = utils.inputHelp("省份")
    street = utils.inputHelp("街道")
    door = utils.inputHelp("门牌号")
    money = int(input("银行卡存款余额:"))

    status = bank.bank_addUser(username, password, country, province, street, door, money)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        sql = "select * from user where username=%s"
        param = [username]
        data = select(sql, param, mode="all")
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
#存钱
def saveMoney():
    inaccuser = utils.inputHelp("用户的账号：")

    inaccmoney = int(input("请输入存去的金额："))

    status = bank.bank_inmoney(inaccuser, inaccmoney)

    status == False

#取钱
def takeMoney():
    outaccuser = utils.inputHelp("用户的账号：")

    outpassword = utils.inputHelp("用户的密码：")

    outusermoney = int(input("请输入取钱金额："))

    status = bank.bank_outmoney(outaccuser, outpassword, outusermoney)

    if status == 1:
        print("该用户不存在！")
    if status == 2:
        print("密码不正确！")
    if status == 3:
        print("账户余额不足！")

    # pass
#转账
def transMoney():
    outacc = utils.inputHelp("转出的账号：")

    inacc = utils.inputHelp("转入的账号：")

    outpassword = utils.inputHelp("转出账号的密码：")

    outmoney = int(input("请输入转出的金额："))

    status = bank.bank_outaccin(outacc, inacc, outpassword, outmoney)

    if status == 1:
        print("该用户不存在")
    elif status == 2:
        print("密码不正确！")
    elif status == 3:
        print("转出账户金额不足，无法转账！")
    elif status == 4:
        print("转账成功！")

#查询
def selectUser():
    insertuser = utils.inputHelp("用户账号：")

    insertuserpwd = utils.inputHelp("账号密码：")

    status = bank.bank_insert(insertuser, insertuserpwd)

    status == None


while True:
    # 欢迎页面
    welcome.print_welcome()

    #用户选择:程序入口
    chose = utils.inputHelp("选项")
    if bank.isExists(chose,bank.bank_choose):
        if chose == "1":
            addUser()
        elif chose == "2":
            saveMoney()
        elif chose == "3":
            takeMoney()
        elif chose == "4":
            transMoney()
        elif chose  == "5":
            selectUser()
        elif chose == "6":
            print("Bye!欢迎下次光临！")
            break
    else:
        print("不存在改选项，被瞎弄！")