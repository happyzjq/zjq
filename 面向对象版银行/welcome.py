from Bank import Bank
welcome = '''
*******************************
*    中国工商银行账户管理系统    *
*******************************
*           选项              *
'''
welcome_item ='''*           {0}.{1}           *'''
# 欢迎类
class Welcome:

    def print_welcome(self):
        print(welcome)
        keys = Bank.bank_choose.keys()
        for key in keys:
            print(welcome_item.format(key,Bank.bank_choose.get(key)))
        print("******************************")