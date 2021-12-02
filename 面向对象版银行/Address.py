# 地址类
class Address():
    __country=None
    __province=None
    __street=None
    __door=None
    def setCountry(self,country):
        self.__country=country
    def getCountry(self):
        return self.__country
    def setProvince(self,province):
        self.__province=province
    def getProvince(self):
        return self.__province
    def setStreet(self,street):
        self.__street=street
    def getStreet(self):
        return self.__street
    def setDoor(self,door):
        self.__door=door
    def getDoor(self):
        return self.__door
