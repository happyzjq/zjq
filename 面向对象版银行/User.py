# 用户类
class User():
    __userID=None
    __username=None
    __password=None
    __address=None
    __money=None
    __registertime=None
    __khh=None
    def setUserID(self,userID):
        self.__userID=userID
    def getUserID(self):
        return self.__userID
    def setUsername(self,username):
        self.__username=username
    def getUsername(self):
        return self.__username
    def setPassword(self,password):
        self.__password=password
    def getPassword(self):
        return self.__password
    def setAddress(self,address):
        self.__address=address
    def getAddress(self):
        return self.__address
    def setMoney(self,money):
        self.__money=money
    def getMoney(self):
        return self.__money
    def setRegistertime(self,registertime):
        self.__registertime=registertime
    def getRegistertime(self):
        return self.__registertime
    def setKhh(self,khh):
        self.__khh=khh
    def getKhh(self):
        return self.__khh

