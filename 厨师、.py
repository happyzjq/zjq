
#定义厨师类
class chef:
    __username = ""
    __age = 0

    def setUsername(self,username):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return self.__age
    #蒸饭的方法
    def steamRice(self):
        print("蒸大米饭！！！！")

#厨师的子类
class chefOffSpring(chef):
    #炒菜的方法
    def cook(self):
        print("炒西红柿！！！！")

#厨师子类的子类
class cookOff(chefOffSpring):
    #重写厨师类的蒸饭方法
    def steamRice(self):
        print("蒸饭",end='')
    #重写厨师子类的炒菜方法
    def cook(self):
        print("炒西红柿")

#测试类
class test:
    c = cookOff()
    c.setUsername("崔鹏飞")
    c.setAge(23)
    print(c.getUsername(),"厨师，今年",c.getAge(),"岁了！！！！")
    print("他当厨师至今，才只学会了",end='')
    c.steamRice()
    print("和",end='')
    c.cook()
    print("悟性真差，不适合当厨子呀！！！！")


test()