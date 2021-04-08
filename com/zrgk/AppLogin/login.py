#coding:utf-8
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:21503",
    "app": "E:\word\shidonghui.apk",
    # "appWaitActivity":"cn.com.open.mooc.index.splash.GuideActivity"
    # 直接登录，去除广告滑动
    "noReset": "true"
    }
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
time.sleep(5)

time.sleep(4)
# self.driver.find_element_by_id("com.huitong.privateboard:id/iv_close").click()
page = ("id", "com.huitong.privateboard:id/iv_close")
my = ("id", "com.huitong.privateboard:id/shidong_me")
wallet = ("id", "com.huitong.privateboard:id/item_image")
login = ("id", "com.huitong.privateboard:id/btn_login")
pwdLogin = ("id", "com.huitong.privateboard:id/tv_password_login")
username = ("id", "com.huitong.privateboard:id/et_phone")
password = ("id", "com.huitong.privateboard:id/et_password")
submit = ("id", "com.huitong.privateboard:id/btn_login")
prompt = ("id", "com.huitong.privateboard:id/cancel")
setUp = ("id", "com.huitong.privateboard:id/tv_settings")
signOut = ("id", "com.huitong.privateboard:id/ll_logout")
confirm = ("id", "com.huitong.privateboard:id/confirm")

WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(page)).click()
WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(my)).click()
WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(wallet)).click()
WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(login)).click()
WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(pwdLogin)).click()
WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(username)).send_keys("12345678911")
WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(password)).send_keys("123456")
WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(submit)).click()
# WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located(prompt)).click()
WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(setUp)).click()
WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(signOut)).click()
WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(confirm)).click()