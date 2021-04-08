#coding:utf-8
import time
from appium import webdriver
from AppiumPython.util.write_user_command import WriteUserCommand

#启动APP
class BaseDriver:
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

if __name__ == '__main__':
    login = BaseDriver()
    login.android_driver()


    # def ios_driver(self):
    #     pass
    # def get_driver(self):
    #     pass

# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

# print tinydict.values(),
#
# print tinydict.keys()

# list1 = [1,2,3,4,5,6,8,9]
# list2 = [1,5,"sdfg",7,2,"djfps"]

# data = list1.remove()
# print list1[::-1]
# list1.reverse()
# print list1

# print cmp(list1,list2)

# print list1.extend(list2)

# localtime = time.localtime(time.time())
# print localtime

# str = raw_input("输入：")
# str = input("输入：")
# print str