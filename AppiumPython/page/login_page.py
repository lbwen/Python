#coding:utf-8
import time
from AppiumPython.util.get_by_local import GetByLocal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AppiumPython.base.base_driver import BaseDriver
class LoginPage:
    #获取登录页面所有的页面元素信息
    def __init__(self,i):
        base_driver = BaseDriver()
        self.driver = BaseDriver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)         #GetByLocal：获取定位信息，如：id，ClassName
    def get_username_element(self):
        #获取用户名元素信息
        return self.get_by_local.get_element("username")
    def get_password_element(self):
        #获取密码元素信息
        return self.get_by_local.get_element("password")
    def get_login_button_element(self):
        #获取登录元素信息
        return self.get_by_local.get_element("login_button")
    def get_forget_password_element(self):
        #忘记密码
        return self.get_by_local.get_element("forget_password")
    def get_register_element(self):
        #注册元素
        return self.get_by_local.get_element("")
    def get_tost_element(self,message):
        time.sleep(2)
        tost_element = ("xpath", "//*[contains(@text,"+message+")]")
        return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(tost_element))