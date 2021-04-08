#coding:utf-8
from AppiumPython.handle.login_handle import LoginHandle
# from AppiumPython1.bussiness.manua_input import Manua
class LoninBusiness:
    def __init__(self,i):
        self.login_handle = LoginHandle(i)      #LoginHandle：操作登录页面元素，输入用户名和密码

    #输入账号和密码，点击登录
    def login_pass(self):
        #send_username      self.login_page.get_username_element().send_keys(user)
        self.login_handle.send_username("12345678913")
        self.login_handle.send_password("123456")
        self.login_handle.click_login()

