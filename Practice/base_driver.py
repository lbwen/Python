#coding:utf-8
import time
from appium import webdriver
from AppiumPython.util.write_user_command import WriteUserCommand

#启动APP
class BaseDriver:
    def __init__(self):
        print "a"
    # def __init__(self,i):
    #     self.login_handle = LoginHandle(i)      #LoginHandle：操作登录页面元素，输入用户名和密码

    #输入账号和密码，点击登录
    # def login_pass(self):
    #     #send_username      self.login_page.get_username_element().send_keys(user)
    #     self.login_handle.send_username("12345678913")
    #     self.login_handle.send_password("123456")
    #     self.login_handle.click_login()

    def android_driver(self):
        #devices_name  adb devices
        #port
        # write_file = WriteUserCommand()
        # devices = write_file.get_value('user_info_'+str(i),'deviceName')
        # port = write_file.get_value('user_info_'+str(i),'port')
        capabilities = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:21503",
            "app": "E:\word\shidonghui.apk",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(10)
        return driver

# if __name__ == '__main__':
#     driver = BaseDriver().android_driver()
    #driver.android_driver()
    # driver.login_pass()

    # def ios_driver(self):
    #     pass
    # def get_driver(self):
    #     pass