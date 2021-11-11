'''
商城系统：
    列表：容器来存储数据
    for循环：遍历数据
    if...else：
1.技术选型：

2.需求
    1.准备一个货架，摆上很多商品
    2.准备一个空的购物车
    3.钱包还的有钱


    4.买东西
        1.如果有这个商品
            判断余额足够买这个东西
                够买
                    余额减去商品的价格
                    购物车添加这个商品
                    温馨提示：成功添加购物车！
                不够：
                    穷鬼，买啥？？？
                是否输入的是q或者Q:
                    退出！
        2.如果没有这个商品
            温馨：没有这个商品，别瞎弄！


    5.打印购物小条！


任务1：
    改造购物小条，将多条重复显示，优化成 yyyyyyy   xn
'''
import random
shop = [
    ["牙膏",21.5],
    ["lenovo",4500],
    ["Mac pro",12000],
    ["Iphone 18 max Pro",56000],
    ["海尔洗衣机",2500],
    ["辣条",3],
    ["洗衣粉",25],
    ["利群",160],
    ["红塔山",130]
]

vshop = [
    ["牙膏",21.5],
    ["lenovo",4500],
    ["Mac pro",12000],
    ["Iphone 18 max Pro",56000],
    ["海尔洗衣机",2500],
    ["辣条",3],
    ["洗衣粉",25],
    ["利群",160],
    ["红塔山",130]
]
a = random.randint(0,10) # 随机获取0-10张优惠券
print("恭喜你幸运的获得了%d张优惠券"%a)
b = random.randint(0,10) # 随机获取折扣
print("每张优惠券折扣为%d折"%b)
c = random.randint(0,8) #随机获取vshop中的一种商品为折扣商品
d = vshop[c][0]
print("获取的优惠券为%s卷"%d)

mycart = []  # 空的购物车

# 初始化余额
salary = input("请输入您的钱包余额：") # "356"  -->  356
sal = salary = int(salary)   # "356" --> 356


while True:
    # 展示商品架
    for key,value in enumerate(shop):
        print(key,value)

    chose = input("请输入您要买的商品编号：") # "9aa" --> 9
    if chose.isdigit():
        chose = int(chose)
        if chose >= len(shop):
            print("温馨提示：这个商品不存在！别瞎弄！")
        else:
            if  a > 0 and chose == c:
                vshop[c][1] = b * shop[c][1] * 0.1
                a = a-1
                print("%s优惠券还剩%s张" % (d , a))
                if salary < vshop[chose][1]:
                    print("温馨提示：穷鬼，没钱，别瞎买！")
                else:
                    salary = salary - vshop[chose][1]
                    mycart.append(vshop[chose])
                    print(vshop[chose][0],"添加购物车成功！余额还剩:￥",salary)
            else:
                if salary < shop[chose][1]:
                    print("温馨提示：穷鬼，没钱，别瞎买！")
                else:
                    salary = salary - shop[chose][1]
                    mycart.append(shop[chose])
                    print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break  # 跳出循环
    else:
        print("兄弟，商品不存在！别瞎弄！")


# 打印购物小条
print("----------------欢迎下次光临Jason小商店--------------")
print("以下是您的购物小条，请拿好：")
print("--------------------------------------------------")
# for key,value in enumerate(mycart):
#     print(key,value)
myct = []

for i in mycart:
    if i not in myct:
        myct.append(1)
        print(" %s x %s " % (i, mycart.count(i)))
print("-------------------------------------------------")
print("您本次还剩余额为：￥",salary,"，本次消费：￥",(sal - salary))











