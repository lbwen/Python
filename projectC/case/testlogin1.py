#coding:utf-8
from selenium import webdriver
from projectC.page.loginchandao import LoginPage,url
import time
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.open(url)

    def test_01(self):
        self.login_driver.input_username("test")
        self.login_driver.input_psw("123456")
        # 第3步：点击登录按钮
        self.login_driver.click_login_button()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()
#
# if __name__ == "__main__":
#     unittest.main()