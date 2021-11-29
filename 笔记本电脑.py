import time

class computer:
    __srceen = 0.0
    __price = 0.0
    __cpu = ""
    __memory = 0.0
    __standby = 0.0

    def setSrceen(self,srceen):
        if self.__srceen > 20 and self.__srceen < 0:
            print("你这叫笔记本电脑？有这么大的屏幕吗，。。。。。。。。。。。那叫显示器")
        else:
            self.__srceen = srceen

    def getSrceen(self):
        return self.__srceen

    def setPrice(self,price):
        if self.__price < 0:
            print("败家玩意！！电脑有卖负价钱的吗，多少买卖都不够你赔的。。。。。。。。。。。。")
        else:
            self.__price = price

    def getPrice(self):
        return self.__price

    def setCpu(self,cpu):
        self.__cpu = cpu

    def getCpu(self):
        return self.__cpu

    def setMemory(self,memory):
        if self.__memory < 0:
            print("...........你也是人才了，内存为负数，咋想的呢！！！！！")
        else:
            self.__memory = memory

    def getMemory(self):
        return self.__memory

    def setStandby(self,standby):
        if self.__standby < 0:
            print(".............人才已经无法形容你了，负待机时长，被人买它是来拿板砖用的吗!!!!")
        else:
            self.__standby = standby

    def getStandby(self):
        return self.__standby

    def typing(self):
        print("新买的笔记本电脑，",self.__srceen,"寸的屏幕，",self.__cpu,"的CPU型号，",self.__standby,"小时的待机时长，")
        print("花了我",self.__price,"大洋")
        print("我要打字爽爽！！！！嘿嘿额嘿嘿额---》》》》")

    def playgame(self):
        print("新电脑挺不错的，",self.__cpu,"的CPU，我要打个原神爽爽，看看运行速度咋样-_-!!!!嘿嘿嘿")
        for i in range(1,6):
            print(".",end="")
            time.sleep(1)
        print("欢迎来到！！！原神世界")

    def watchwideo(self):
        print(self.__srceen,"的屏幕，看红色通缉真爽！！！！哈哈哈哈哈哈啊哈哈哈。。。。。。")

a = computer()

a.setSrceen(15.1)
a.setCpu("骁龙855")
a.setMemory(16)
a.setStandby(24)
a.setPrice(8600)

a.playgame()
a.typing()
a.watchwideo()