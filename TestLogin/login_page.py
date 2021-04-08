#coding:utf-8
from login_to import LoginTo
from appium import webdriver
class LoginPage:
    def __init__(self):
        self.driver = LoginTo()
        self.driver.android_driver()


#点击操作
    def login_page(self):

        self.driver.find_element_by_id("com.huitong.privateboard:id/shidong_me").click()
        # elements = driver.find_elements_by_class_name("android.widget.TextView")
        # elements[2].click()
        elements = self.driver.find_elements_by_class_name("android.widget.TextView")
        elements[2].click()
        self.driver.find_element_by_id("com.huitong.privateboard:id/btn_login").click()
        self.driver.find_element_by_id("com.huitong.privateboard:id/tv_password_login").click()
        # return driver

if __name__ == '__main__':
    a = LoginPage()
    a.login_page()
    # LoginPage.login_page()