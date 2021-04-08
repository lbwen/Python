#coding=utf-8
from appium import webdriver
import  time

def get_driver():
    capabilities = {
        "platformName" : "Android",
        "deviceName" : "127.0.0.1:21503",
        "app" : "E:\\apk\\shidonghui.apk",
        # "appWaitActivity": "cn.com.open.mooc.user.register.MCPhoneRegisterAty",
        "noReset": "true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
    return driver

# 获取屏幕的宽高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width , height

def swipe_left():
    x1 = get_size()[0]/10*9
    y = get_size()[1]/2
    x = get_size()[0]/10
    driver.swipe(x1,y,x,y,3000)

def swipe_right():
    x1 = get_size()[0]/10
    y = get_size()[1]/2
    x = get_size()[0]/10*9
    driver.swipe(x1,y,x,y,3000)

def swipe_up():
    y1 = get_size()[0] / 10 * 9
    x = get_size()[1] / 2
    y = get_size()[0] / 10
    driver.swipe(x, y1, x, y, 3000)

def swipe_down():
    y1 = get_size()[0] / 10
    x = get_size()[1] / 2
    y = get_size()[0] / 10 * 9
    driver.swipe(x, y1, x, y, 3000)

def swipe_on(direction):
    if direction == "left":
        swipe_left()
    elif direction =="right":
        swipe_right()
    elif direction == "down":
        swipe_down()
    else:
        swipe_up()

driver = get_driver()
time.sleep(6)
driver.find_element_by_id("com.huitong.privateboard:id/iv_close").click()
driver.find_element_by_android_uiautomator()
time.sleep(3)
swipe_on("down")
swipe_on("down")
