#coding:utf-8
from login_handle import LoginHandle
# from AppiumPython.bussiness.manua_input import Manua
class LoginBusiness:
    def __init__(self):
        self.login_handle = LoginHandle()      #LoginHandle：操作登录页面元素，输入用户名和密码

    #输入账号和密码，点击登录
    def login_pass(self):
        #send_username      self.login_page.get_username_element().send_keys(user)
        self.login_handle.send_username("12345678913")
        self.login_handle.send_password("123456")
        self.login_handle.click_login()

# if __name__ == '__main__':
#     driver = LoginBusiness()
#     #driver.android_driver()
#     driver.login_pass()

