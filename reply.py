#coding:utf-8
import time
import uniout
import os
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MessageReply:
    # def __init__(self):
    #     'unicodeKeyboard':True,  # 使用unicodeKeyboard的编码方式来发送字符串
    #     'resetKeyboard':True  # 将键盘给隐藏起来
    #     capabilities.setCapability("unicodeKeyboard", "True");
    #     capabilities.setCapability("resetKeyboard", "True");
    #
    #     desired_caps["unicodeKeyboard"] = "True"
    #     desired_caps["resetKeyboard"] = "True"
    def timing_start(self):
        path = r'E:\Program Files\Microvirt\MEmu\MEmu.exe'   #打开模拟器
        os.startfile(path)
        time.sleep(50)

    def start_up(self):
        capabilities = {
            "platformName": "Android",
	        #"automationName":"UiAutomator2",
	        "deviceName": "127.0.0.1:21503",
	        "app" : "E:\\apk\\app-dev-release.apk",
            "unicodeKeyboard":"True",   # 使用unicodeKeyboard的编码方式来发送字符串
            "resetKeyboard":"True",     # 将键盘给隐藏起来
	        # "appWaitActivity":"cn.com.open.mooc.user.register.MCPhoneRegisterAty",
	        "noReset":"true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
        time.sleep(5)
        # return self.driver

    def login(self):
        # listcanOffer = ("id", "listcanOffer")
        # WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(listName)).send_keys(ldata["name"])
        # iv_close = ("id","com.huitong.privateboard:id/iv_close")
        # shidong_me = ("id","com.huitong.privateboard:id/shidong_me")
        # item_layout = ("id","com.huitong.privateboard:id/item_layout")
        # btn_login = ("id","com.huitong.privateboard:id/btn_login")
        # tv_password_login = ("id","com.huitong.privateboard:id/tv_password_login")
        # et_phone = ("id","com.huitong.privateboard:id/et_phone")
        # et_password = ("id","com.huitong.privateboard:id/et_password")
        # btn_login1 = ("id","com.huitong.privateboard:id/btn_login")
        # tab_text_chats_press = ("id","com.huitong.privateboard:id/tab_text_chats_press")

        phoneNumber = "12345678913"
        Pword = "123456"
        HomePageLogin = ("id", "com.huitong.privateboard:id/tv_user_name")
        SignIn = ("id", "com.huitong.privateboard:id/btn_login")
        PasswordLogin = ("id", "com.huitong.privateboard:id/tv_password_login")
        UserName = ("id", "com.huitong.privateboard:id/et_phone")
        PassWord = ("id", "com.huitong.privateboard:id/et_password")
        Longin = ("id", "com.huitong.privateboard:id/btn_login")
        News = ("id", "com.huitong.privateboard:id/shidong_chat")  # 消息

        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(HomePageLogin)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(SignIn)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(PasswordLogin)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(UserName)).send_keys(phoneNumber)
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(PassWord)).send_keys(Pword)
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(Longin)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(News)).click()

        # WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(iv_close)).click()
        # WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(shidong_me)).click()
        # WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(item_layout)).click()
        # WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(btn_login)).click()
        # WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(tv_password_login)).click()
        # WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(et_phone)).send_keys("12345678913")
        # WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(et_password)).send_keys("123456")
        # WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(btn_login1)).click()
        # WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(tab_text_chats_press)).click()

    #回复公司群
    def company_group(self):
        Wenanceshi = ('xpath','//android.widget.TextView[@text="Wenanceshi"]')
        rc_edit_text = ("id","com.huitong.privateboard:id/rc_edit_text")
        rc_send_toggle = ("id","com.huitong.privateboard:id/rc_send_toggle")
        iv_back = ("id", "com.huitong.privateboard:id/iv_back")

        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(Wenanceshi)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(rc_edit_text)).send_keys(u"收到已转发")
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(rc_send_toggle)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(iv_back)).click()

    #回复体验群
    def experience_group(self):
        experience = ('xpath','//android.widget.TextView[@text="测试文案字数"]')
        rc_edit_text = ("id", "com.huitong.privateboard:id/rc_edit_text")
        rc_send_toggle = ("id", "com.huitong.privateboard:id/rc_send_toggle")
        iv_back = ("id", "com.huitong.privateboard:id/iv_back")

        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(experience)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(rc_edit_text)).send_keys(u"👍👍👍")
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(rc_send_toggle)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(iv_back)).click()

    # 退出登录
    def log_out(self):
        Me = ("id", "com.huitong.privateboard:id/shidong_me")
        SetUp = ("id", "com.huitong.privateboard:id/iv_setting")
        LogOut = ("id", "com.huitong.privateboard:id/ll_logout")
        Confirm = ("id", "com.huitong.privateboard:id/confirm")

        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(Me)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(SetUp)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(LogOut)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(Confirm)).click()

    #关闭应用程序
    def close_app(self):
        os.system("taskkill /F /IM MEmu.exe")

    #滑动
    def slide(self):
        # 获取屏幕的宽高
        def get_size():
            size = self.driver.get_window_size()
            width = size['width']
            height = size['height']
            return width, height

        # 向左滑动
        def swipe_left():
            # [100,200]
            x1 = get_size()[0] / 10 * 9
            y1 = get_size()[0] / 10*9
            x = get_size()[0] / 10
            self.driver.swipe(x1, y1, x, y1)
        swipe_left()

if __name__ == '__main__':
    mess = MessageReply()
    mess.timing_start()
    mess.start_up()
    mess.login()
    mess.company_group()
    mess.experience_group()
    mess.log_out()
    mess.close_app()