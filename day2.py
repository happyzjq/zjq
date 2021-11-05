'''
在注释里增加：
1、猜的数字是系统产生，不是自己定义
            使用random随机数技术来获取随机数
 范围：0~150
    猜10次！
    如果输入大了：温馨提示：大了
    如果输入小了：温馨提示：小了
    正好猜中，恭喜您，猜中，本次猜的数字为xxxx。
操作完成之后才增加：
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定。猜中加3000。
'''
import random
Ran = random.randint(0,50)
print(Ran)
i = 0
znum = 5000
while i<16:
    num = input("请输入你猜的数字：")
    num = int(num)

    if num ==Ran:
        znum = znum + 3000
        print("猜中了")
        print("剩余金币：", znum)
        # break
    elif num > Ran:
        znum = znum - 500
        print("猜大了")
        print("剩余金币：", znum)
    elif num <Ran:
        znum = znum - 500
        print("猜小了")
        print("剩余金币：", znum)
    if znum == 0:
        print("你没钱了，金币已经扣光")
        break

    i = i + 1