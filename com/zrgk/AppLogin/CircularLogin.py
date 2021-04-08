#coding:utf-8
import time
import ddt
import unittest
from selenium import webdriver
import HTMLTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AccountNumber import ExcelR

data = ExcelR("user.xlsx")
ldata = data.dict_data()

@ddt.ddt
class Tandao(unittest.TestCase):
    def setUp(self):
        cap = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:21503",
            "app": "E:\word\shidonghui.apk",
            # "appWaitActivity":"cn.com.open.mooc.index.splash.GuideActivity"
            # 直接登录，去除广告滑动
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
        time.sleep(5)
        return self.driver

    @ddt.data(*ldata)
    def testLogin(self, ldata):
        time.sleep(4)
        # self.driver.find_element_by_id("com.huitong.privateboard:id/iv_close").click()
        page = ("id","com.huitong.privateboard:id/iv_close")
        my = ("id","com.huitong.privateboard:id/shidong_me")
        wallet = ("id","com.huitong.privateboard:id/item_image")
        login = ("id","com.huitong.privateboard:id/btn_login")
        pwdLogin = ("id","com.huitong.privateboard:id/tv_password_login")
        username = ("id","com.huitong.privateboard:id/et_phone")
        password = ("id","com.huitong.privateboard:id/et_password")
        submit = ("id","com.huitong.privateboard:id/btn_login")
        prompt = ("id","com.huitong.privateboard:id/cancel")
        setUp = ("id","com.huitong.privateboard:id/tv_settings")
        signOut = ("id","com.huitong.privateboard:id/ll_logout")
        confirm = ("id","com.huitong.privateboard:id/confirm")

        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(page)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(my)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(wallet)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(login)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(pwdLogin)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(username)).send_keys(ldata["name"])
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(password)).send_keys(ldata["pwd"])
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(submit)).click()
        WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located(prompt)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(setUp)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(signOut)).click()
        WebDriverWait(self.driver, 10 ,1).until(EC.presence_of_element_located(confirm)).click()
        time.sleep(10)

    def tearDown(self):
        print "已登录"

if __name__ == '__main__':
    unittest.main()