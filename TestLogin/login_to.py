#coding:utf-8
from appium import webdriver
import time

class LoginTo:
    def android_driver(self):
        capabilities = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:21503",
            "app": "E:\word\shidonghui.apk",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(5)
        # return self.driver

    # 点击操作
    def login_page(self):
        self.driver.find_element_by_id("com.huitong.privateboard:id/shidong_me").click()
        # elements = driver.find_elements_by_class_name("android.widget.TextView")
        # elements[2].click()
        elements = self.driver.find_elements_by_class_name("android.widget.TextView")
        elements[2].click()
        self.driver.find_element_by_id("com.huitong.privateboard:id/btn_login").click()
        self.driver.find_element_by_id("com.huitong.privateboard:id/tv_password_login").click()
    #输入账号和密码
    def login_business(self):
        self.driver.find_element_by_id("com.huitong.privateboard:id/et_phone").send_keys("12345678914")
        self.driver.find_element_by_id("com.huitong.privateboard:id/et_password").send_keys("123456")
        self.driver.find_element_by_id("com.huitong.privateboard:id/btn_login").click()

if __name__ == '__main__':
    loginto = LoginTo()
    loginto.android_driver()
    loginto.login_page()
    # loginto.login_business()
