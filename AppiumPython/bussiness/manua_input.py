#coding:utf-8
from AppiumPython1.bussiness.login_business import LoninBusiness
class Manua:
    def __init__(self,driver):
        self.manua_input = LoninBusiness(driver)
    def input_name(self):
        name = input("请输入账号：")
        return name
        # self.manua_input.login_pass(name)
        password = input("请输入密码")
        self.manua_input.login_pass(password)