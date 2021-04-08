#coding:utf-8
import time
from appium import webdriver
from AppiumPython.util.write_user_command import WriteUserCommand

#启动APP
class BaseDriver:
    def android_driver(self,i):
        #devices_name  adb devices
        #port
        write_file = WriteUserCommand()
        devices = write_file.get_value('user_info_'+str(i),'deviceName')
        port = write_file.get_value('user_info_'+str(i),'port')
        capabilities = {
            "platformName": "Android",
            "deviceName": devices,
            "app": "E:\word\shidonghui.apk",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub", capabilities)
        time.sleep(10)
        return driver


    # def ios_driver(self):
    #     pass
    # def get_driver(self):
    #     pass