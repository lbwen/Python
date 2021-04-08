#coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AppiumPython1.util.read_init import ReadIni
from AppiumPython1.util.get_by_local import GetByLocal
def get_driver():
    cap = {
        "platformName":"Android",
        "deviceName":"127.0.0.1:21503",
        "app":"E:\word\shidonghui.apk",
        "noReset":"true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
    time.sleep(5)
    return driver
def login():
    driver.find_element_by_id("com.huitong.privateboard:id/shidong_me").click()
    elements = driver.find_elements_by_class_name("android.widget.TextView")
    elements[2].click()
    driver.find_element_by_id("com.huitong.privateboard:id/btn_login").click()
    driver.find_element_by_id("com.huitong.privateboard:id/tv_password_login").click()

    get_by_local = GetByLocal(driver)
    get_by_local.get_element("username").send_keys("12345678913")
    get_by_local.get_element("password").send_keys("123456")
    get_by_local.get_element("login_button").click()
driver = get_driver()
login()