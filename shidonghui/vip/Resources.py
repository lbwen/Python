#coding:utf-8
import ddt
import time
import uniout
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_phone import ExcelR

data = ExcelR("phone.xlsx")
ldata = data.dict_data()
@ddt.ddt
class Resources(unittest.TestCase):
    def setUp(self):
        print "开始"

    @ddt.data(*ldata)
    def test_login(self,ldata):
        capabilities = {
            "platformName": "Android",
            # "automationName":"UiAutomator2",
            "deviceName": "127.0.0.1:21503",
            "app": "E:\\word\\shidonghui.apk",
            # "appWaitActivity":"cn.com.open.mooc.user.register.MCPhoneRegisterAty",
            "unicodeKeyboard": "True",  # 使用unicodeKeyboard的编码方式来发送字符串
            "resetKeyboard": "True",  # 将键盘给隐藏起来
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(5)
        # return self.driver

        tab_img_me_press = ("id", "com.huitong.privateboard:id/tab_img_me_press") #我的
        item_image = ("id", "com.huitong.privateboard:id/item_image") #我的购买
        btn_login = ("id", "com.huitong.privateboard:id/btn_login") #登录
        tv_password_login = ("id", "com.huitong.privateboard:id/tv_password_login") #密码登录
        et_phone = ("id", "com.huitong.privateboard:id/et_phone") #输入手机号
        et_password = ("id", "com.huitong.privateboard:id/et_password") #输入密码
        btn_login_go = ("id", "com.huitong.privateboard:id/btn_login") #点击登录
        tv_update = ("id", "com.huitong.privateboard:id/tv_update") #升级用户
        tv_update_lj = ("id", "com.huitong.privateboard:id/tv_update")  # 立即升级
        rl_ali_pay = ("id", "com.huitong.privateboard:id/rl_ali_pay")  # 选择支付宝
        confirm_pay = ("id", "com.huitong.privateboard:id/confirm_pay")  # 确认支付

        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(tab_img_me_press)).click()
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(item_image)).click()
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(btn_login)).click()
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(tv_password_login)).click()
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(et_phone)).send_keys(ldata["phone"])
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(et_password)).send_keys("123456")
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(btn_login_go)).click()
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(tv_update)).click()
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(tv_update_lj)).click()
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(rl_ali_pay)).click()
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(confirm_pay)).click()

    def tearDown(self):
        print "完成"

if __name__ == '__main__':
    unittest.main()