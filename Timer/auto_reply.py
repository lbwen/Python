#coding:utf-8
import os
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutoRepiy:
    def timing_start(self):
        while True:
            time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
            if time_now == "16:51:00":  # 此处设置每天定时的时间
                # os.system("kill task sometask")
                path = r'E:\Program Files\Microvirt\MEmu\MEmu.exe'   #打开模拟器
                os.startfile(path)
                time.sleep(50)
            elif time_now == "17:06:00":
                path = r'E:\Program Files\Microvirt\MEmu\MEmu.exe'  # 打开模拟器
                os.startfile(path)
                time.sleep(50)
                break

    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            # "automationName":"UiAutomator2",
            "deviceName": "127.0.0.1:21503",
            "app": "E:\\apk\\app-dev-release.apk",
            # "appWaitActivity": "cn.com.open.mooc.user.register.MCPhoneRegisterAty",
            "unicodeKeyboard": "True",  # 使用unicodeKeyboard的编码方式来发送字符串
            "resetKeyboard": "True",  # 将键盘给隐藏起来
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(10)
        return self.driver

    def get_login(self):
        phoneNumber = "15776717571"
        Pword = "123456"
        HomePageLogin = ("id", "com.huitong.privateboard:id/tv_user_name")
        SignIn = ("id", "com.huitong.privateboard:id/btn_login")
        PasswordLogin = ("id", "com.huitong.privateboard:id/tv_password_login")
        UserName = ("id", "com.huitong.privateboard:id/et_phone")
        PassWord = ("id", "com.huitong.privateboard:id/et_password")
        Longin = ("id", "com.huitong.privateboard:id/btn_login")
        News = ("id", "com.huitong.privateboard:id/shidong_chat")  # 消息
        # experience = ('xpath', '//android.widget.TextView[@text="师董会公司群"]')
        # experience1 = ('xpath', '//android.widget.TextView[@text="师董会APP体验群"]')
        # InputBox = ("id", "com.huitong.privateboard:id/rc_edit_text")  # 点击输入框
        # rc_send_toggle = ("id", "com.huitong.privateboard:id/rc_send_toggle")  # 发送
        # iv_back = ("id", "com.huitong.privateboard:id/iv_back")  # 返回

        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(HomePageLogin)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(SignIn)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(PasswordLogin)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(UserName)).send_keys(phoneNumber)
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(PassWord)).send_keys(Pword)
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(Longin)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(News)).click()
        # WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(rc_edit_text)).send_keys(u"👍👍👍")  #点赞

    # 回复公司群
    def company_group(self):
        Wenanceshi = ('xpath', '//android.widget.TextView[@text="师董会公司群"]')
        rc_edit_text = ("id", "com.huitong.privateboard:id/rc_edit_text")
        rc_send_toggle = ("id", "com.huitong.privateboard:id/rc_send_toggle")  # 发送
        iv_back = ("id", "com.huitong.privateboard:id/iv_back")  # 返回

        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(Wenanceshi)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(rc_edit_text)).send_keys(u"收到已转发")
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(rc_send_toggle)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(iv_back)).click()

    # 回复体验群
    def experience_group(self):
        experience = ('xpath', '//android.widget.TextView[@text="师董会APP体验群"]')
        rc_edit_text = ("id", "com.huitong.privateboard:id/rc_edit_text")
        rc_send_toggle = ("id", "com.huitong.privateboard:id/rc_send_toggle")  # 发送
        iv_back = ("id", "com.huitong.privateboard:id/iv_back")  # 返回

        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(experience)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(rc_edit_text)).send_keys(u"👍👍👍")
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(rc_send_toggle)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(iv_back)).click()

    #退出登录
    def log_out(self):
        Me = ("id", "com.huitong.privateboard:id/shidong_me")
        SetUp = ("id", "com.huitong.privateboard:id/iv_setting")
        LogOut = ("id", "com.huitong.privateboard:id/ll_logout")
        Confirm = ("id", "com.huitong.privateboard:id/confirm")

        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(Me)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(SetUp)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(LogOut)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(Confirm)).click()

    # 关闭应用程序
    def close_app(self):
        os.system("taskkill /F /IM MEmu.exe")


if __name__ == '__main__':
    mess = AutoRepiy()
    mess.timing_start()
    mess.get_driver()
    mess.get_login()
    mess.company_group()
    mess.experience_group()
    mess.log_out()
    mess.close_app()
