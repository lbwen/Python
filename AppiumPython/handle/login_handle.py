#coding:utf-8
from AppiumPython.page.login_page import LoginPage
class LoginHandle:
    def __init__(self,i):
        self.login_page = LoginPage(i)      #LoginPage：获取登录页面所有的页面元素信息，用户名、密码
    #操作登录页面元素
    def send_username(self,user):
        #输入用户名
        # get_username_element()获取用户名元素信息
        self.login_page.get_username_element().send_keys(user)
    def send_password(self,password):
        #输入密码
        self.login_page.get_password_element().send_keys(password)
    def click_login(self):
        #点击登录按钮
        self.login_page.get_login_button_element().click()
    def click_forget_password(self):
        #点击忘记密码
        self.login_page.get_forget_password_element().click()