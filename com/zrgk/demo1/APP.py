#coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def get_driver():
    cap = {
        "platformName":"Android",
        "deviceName":"127.0.0.1:21503",
        "app":"E:\word\shidonghui.apk",
        # "appWaitActivity":"cn.com.open.mooc.index.splash.GuideActivity"
        #直接登录，去除广告滑动
        "noReset":"true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",cap)
    time.sleep(5)
    return driver
get_driver()