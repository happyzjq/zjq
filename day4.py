
'''
    导航系统：
        1.字典数据。
        2.方法的使用。

        1.退出：输入q或者Q
任务1：
    将旅游导航系统结合商城系统，集成开发！
    需求：
        当最终到达景点后，询问是否去买纪念品？
            xxxxXXXXxxxxxxxxxxx
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


citys = {
    "北京":{
        "昌平":{
            "十三陵":["十三陵水库"],
            "八达岭":["八达岭长城","野生动物园"],
            "回龙观":["五道口切糕","甑糕","呷哺呷哺","海底捞"]
        },
        "海淀":{
            "高校":["清华","北大"],
            "景点":["香山","植物园"]
        },
        "朝阳":{
            "公园":["玉渊潭公园","朝阳南北塔"]
        },
        "延庆":{
            "景点":["龙庆峡"]
        }
    },
    "上海":{
        "浦东新区":{
            "叶榭市":["外滩公园","外滩"]
        }
    }
}

def showshop(shop):
    # 展示商品架
    print("-----------------请选择您要购买的商品--------------------")
    for key, value in enumerate(shop):
        print(key, value)

def showCity(citys):
    print("---------欢迎来到Jason旅游导航系统！-------------")
    for i in citys:
        print(i)
    print("---------------------------------------")


#
while True:
    showCity(citys)
    chose = input("请输入您想去的一级城市：")
    if chose == 'q' or chose == 'Q':
        print("--------------欢迎下次光临,拜拜嘞你嘞！-------------------")
        break  # 跳出循环
    if chose not in citys:
        print("温馨提示：当前城市没有项目！别瞎弄！")
    else:
        showCity(citys[chose])
        chose2 = input("请输入您想去的二级城市：")
        if chose2 == 'q' or chose2 == 'Q':
            print("--------------欢迎下次光临,拜拜嘞你嘞！-------------------")
            break  # 跳出循环
        if chose2 not in citys[chose]:
            print("都跟你讲了没有这个城市项目，别瞎弄！")
        else:
            showCity(citys[chose][chose2])
            chose3 = input("请输入您想去的三级城市：")
            if chose3 == 'q' or chose3 == 'Q':
                print("--------------欢迎下次光临,拜拜嘞你嘞！-------------------")
                break  # 跳出循环
            if chose3 not in citys[chose][chose2]:
                print("你故意找茬是不是？别瞎弄！")
            else:
                showCity(citys[chose][chose2][chose3])
                print("车已经达到！祝你玩的愉快！")

                while True:
                    chose4 = input("请问你是否要去购买纪念品？：")
                    if chose4 == 'n' or chose4 == 'N':
                        print("好的，欢迎你下次来购买！")
                        break
                    if chose4 == 'y' or chose4 == 'Y':
                        a = random.randint(0, 10)  # 随机获取0-10张优惠券
                        print("恭喜你幸运的获得了%d张优惠券" % a)
                        b = random.randint(0, 10)  # 随机获取折扣
                        print("每张优惠券折扣为%d折" % b)
                        c = random.randint(0, 8)  # 随机获取vshop中的一种商品为折扣商品
                        d = vshop[c][0]
                        print("获取的优惠券为%s卷" % d)

                        mycart = []  # 空的购物车

                        # 初始化余额
                        salary = input("请输入您的钱包余额：")  # "356"  -->  356
                        sal = salary = int(salary)  # "356" --> 356

                        while True:
                            showshop(shop)
                            chose4 = input("请输入您要买的商品编号：")  # "9aa" --> 9
                            if chose4.isdigit():
                                chose4 = int(chose4)
                                if chose4 >= len(shop):
                                    print("温馨提示：这个商品不存在！别瞎弄！")
                                else:
                                    if a > 0 and chose4 == c:
                                        vshop[c][1] = b * shop[c][1] * 0.1
                                        a = a - 1
                                        print("%s优惠券还剩%s张" % (d, a))
                                        if salary < vshop[chose4][1]:
                                            print("温馨提示：穷鬼，没钱，别瞎买！")
                                        else:
                                            salary = salary - vshop[chose4][1]
                                            mycart.append(vshop[chose4])
                                            print(vshop[chose4][0], "添加购物车成功！余额还剩:￥", salary)
                                    else:
                                        if salary < shop[chose4][1]:
                                            print("温馨提示：穷鬼，没钱，别瞎买！")
                                        else:
                                            salary = salary - shop[chose4][1]
                                            mycart.append(shop[chose4])
                                            print(shop[chose4][0], "添加购物车成功！余额还剩:￥", salary)
                            elif chose4 == "q" or chose4 == "Q":
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
                                myct.append(i)
                                print(" %s x %s " % (i, mycart.count(i)))
                        print("-------------------------------------------------")
                        print("您本次还剩余额为：￥", salary, "，本次消费：￥", (sal - salary))
                        print("欢迎下次光临本店！！！！！")
                        print("----------------------------------------------------")
                        print("----------------------------------------------------")
                        print("----------------------------------------------------")
                        print("----------------------------------------------------")
                        print("----------------------------------------------------")
                        break

















































