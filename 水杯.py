class cup:
    __high = 0.0
    __cubage = 0.0
    __color = ""
    __texture = ""

    def setHigh(self,high):
        if self.__high > 0.8 or self.__high <0:
            print("别瞎弄！！！，谁家水杯这么大")
        else:
            self.__high = high

    def getHigh(self):
        return self.__high

    def setCubage(self,cubage):
        if self.__cubage > 1.5 or self.__cubage < 0:
            print("净瞎整！！！！，你这不叫水杯，快赶上桶了")
        else:
            self.__cubage = cubage

    def getCubage(self):
        return self.__cubage

    def setColor(self,color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setTexture(self,texture):
        self.__texture = texture

    def getTexture(self):
        return self.__texture

    def water(self,cubage):
        if cubage > self.__cubage:
            print("多么好的杯子，",self.__high,"的高度，",self.__color,"的颜色，",self.__texture,"的材质")
            print("瞅瞅能干点啥吧你，水杯只能放",self.__cubage,"升水， 放了",cubage,"升水，想啥呢，傻狍子！！！")



a = cup()
a.setHigh(0.5)
a.setColor("青花瓷")
a.setCubage(1)
a.setTexture("皇家瓷釉")

a.water(2)