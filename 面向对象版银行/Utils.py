# 此类是工具类：包括输入帮助和获取8位随机码
import random
class Utils:
    def inputHelp(self, chose, datatype="str"):
        while True:
            print("请输入" + chose + ":")
            i = input(">>>")
            if len(i.strip()) == 0:
                print("该项不能为空，请重新输入！")
                continue
            if datatype != "str":
                return int(i)
            else:
                return i

        # 随机生成8位随机号

    def getRandom(self):

        return random.randint(10000000, 99999999)


# b = Utils()
# v=b.getRandom()
# print(v)
# print(type(v))