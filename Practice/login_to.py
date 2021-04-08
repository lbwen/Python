#coding:utf-8
import time
from appium import webdriver
from AppiumPython.util.write_user_command import WriteUserCommand
from login_business import LoginBusiness
from base_driver import BaseDriver
#启动APP
class LoginTo:
    def login_to(self):
        # self.driver = BaseDriver()
        # self.driver.android_driver()
        # self.init = BaseDriver()
        self.business = LoginBusiness()
        self.business.login_pass()
if __name__ == '__main__':
    # login = LoginTo()
    LoginTo().login_to()


