#coding:utf-8
from selenium import webdriver
from projectC.common.base import BaseC
import time

url=r"http://169.254.28.78:81/zentao/my"
class LoginPage(BaseC):
    #禅道定位
    user_loc =('id','account')
    psw_loc = ("name", "password")
    button_loc = ("xpath", '//button[@id="submit"]')
    # user_loc = ("name", "username")
    # psw_loc = ("name", "password")
    # button_loc = ("class name", "logging")
    # locuser = ("name", "ur_loginName")
    # locpwd = ("name", "ur_password")
    # locbut = ("name", "submit")

    def input_username(self, text):
        self.send_keys(self.user_loc, text, is_clear=True)
    def input_psw(self, text):
        self.send_keys(self.psw_loc, text,is_clear=True)
    def click_login_button(self):
        self.click(self.button_loc)
    def login(self,user=u"admin",pwd="123456"):#参数给了默认值
        self.input_username(user)
        self.input_psw(pwd)
        self.click_login_button()


#
# if __name__ == "__main__":
#     driver = webdriver.Firefox()
#     login_driver = LoginPage(driver)
#     login_driver.open(url)
#     time.sleep(3)
#     login_driver.input_username("admin")
#     login_driver.input_psw("123456")
#     time.sleep(3)
#     login_driver.click_login_button()

