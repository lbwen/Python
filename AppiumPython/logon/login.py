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
# driver.swipe(500,400,50,400)
# driver.swipe(500,400,50,400)
# x1 = width/10*9
# y1 = height/10
# x = width/10
# driver.swipe(x1,y1,x,y1)

#获取屏幕的宽高
# def get_size():
#     size = driver.get_window_size()
#     width = size['width']
#     height = size['height']
#     return width,height
#
# #向左滑动
# def swipe_left():
#     x1 = get_size()[0]/10*9
#     y1 = get_size()[1]/2
#     x = get_size()[0]/10
#     driver.swipe(x1,y1,x,y1)
#
# #向右滑动
# def swipe_right():
#     x1 = get_size()[0]/10
#     y1 = get_size()[1]/2
#     x = get_size()[0]/10*9
#     driver.swipe(x1,y1,x,y1)
#
# #向上滑动
# def swipe_up():
#     x1 = get_size()[0]/2
#     y1 = get_size()[1]/20*18
#     y = get_size()[1]/10
#     driver.swipe(x1,y1,x1,y)
#
# #向下滑动
# def swipe_down():
#     x1 = get_size()[0]/2
#     y1 = get_size()[1]/10
#     y = get_size()[1]/10*9
#     driver.swipe(x1,y1,x1,y)
#
# #定义方向
# def swipe_on(direction):
#     if direction == "on":
#         swipe_up()
#     elif direction == "down":
#         swipe_down()
#     elif direction == "left":
#         swipe_left()
#     else:
#         swipe_right()
# swipe_left()
#登录
def Immediate_experience():
    #点击体验和文字框
    # driver.find_element_by_id("com.huitong.privateboard:id/tv_jump_main").click()
    # time.sleep(1)
    # swipe_on("left")
    # time.sleep(1)
    #登录id = com.huitong.privateboard:id/btn_login
    #点击我的页面
    driver.find_element_by_id("com.huitong.privateboard:id/shidong_me").click()
    time.sleep(1)
    #点击我的页面登录/注册
    # driver.find_element_by_id("com.huitong.privateboard:id/item_layout").click()
    def go_login():
        elements = driver.find_elements_by_class_name("android.widget.TextView")
        elements[2].click()
    go_login()
    time.sleep(1)
    #driver.find_element_by_id("com.huitong.privateboard:id/btn_login").click()
    #用class定位（多个class名称一致）
    def login():
        elements = driver.find_elements_by_class_name("android.widget.TextView")
        elements[3].click()
    login()
    time.sleep(1)
    driver.find_element_by_id("com.huitong.privateboard:id/tv_password_login").click()
    #com.huitong.privateboard:id/tv_verificationcode_login
    #com.huitong.privateboard:id/tv_password_login
    #验证码com.huitong.privateboard:id/et_phone
    #密码com.huitong.privateboard:id/et_phone
    time.sleep(1)
    # driver.find_element_by_id("com.huitong.privateboard:id/et_phone").send_keys("12345678913")
    # time.sleep(1)
    # driver.find_element_by_id("com.huitong.privateboard:id/et_password").send_keys("123456")
    # time.sleep(1)
    #输入手机号和密码（层级定位）
    def by_node():
        element = driver.find_element_by_id("com.huitong.privateboard:id/layout_login")
        elements = element.find_elements_by_class_name("android.widget.EditText")
        elements[0].send_keys("12345678913")
        elements[1].send_keys("123456")
    by_node()
    #点击登录
    driver.find_element_by_id("com.huitong.privateboard:id/btn_login").click()
    time.sleep(5)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("主页")').click()
    # driver.find_element_by_android_uiautomator('new UiSelector().text("想问专家")').click()
    driver.find_element_by_id("com.huitong.privateboard:id/item_layout").click()

#app与H5转换
def get_web_view():
    webview = driver.contexts
    for viw in webview:
        if "WEBVIEW_cn.com.open.mooc" in viw:
            driver.switch_to.context(viw)
            break
    time.sleep(5)
    driver.find_element_by_link_text("立即邀请").click()
    driver.switch_to.context(webview[0])
    driver.find_element_by_id("com.huitong.privateboard:id/iv_back").click()
    # try:
    #     driver.find_element_by_id("com.huitong.privateboard:id/iv_back").click()
    # except Exception as e:
    #     driver.switch_to.context(webview[0])
    #     driver.find_element_by_id("com.huitong.privateboard:id/iv_back").click()
    #     raise e
    print webview

def get_tost():
    time.sleep(3)
    driver.find_element_by_id("com.huitong.privateboard:id/et_phone").send_keys("12345678913")
    tost_element = ("xpath","//*contains(@text,'请填写密码')")
    print WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located(tost_element))
driver = get_driver()
#首次登录广告滑动
# swipe_on("left")
# time.sleep(1)
# swipe_on("left")
# time.sleep(1)
# swipe_on("left")
# time.sleep(1)
Immediate_experience()
# get_web_view()
