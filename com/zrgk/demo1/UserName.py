#coding:utf-8
import uniout
import MySQLdb
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
d = webdriver.Firefox()
d.get(r"http://localhost:8080/jygl_houtai_ZLQ/login.jsp")
time.sleep(1)
d.find_element_by_name("user_loginName").send_keys("xt")
time.sleep(1)
d.find_element_by_name("user_password").send_keys("123")
time.sleep(1)
m = d.find_element_by_xpath("//li[@class='active']")
ActionChains(d).move_to_element(m).perform()
time.sleep(1)
d.find_element_by_xpath("//li[contains(.,'系统管理员')]").click()
time.sleep(1)
d.find_element_by_xpath("//button[@onclick = 'login()']").click()
#点击弹窗的确定
alert=d.switch_to_alert()
##接受
time.sleep(1)
alert.accept()
#点击弹窗的取消
# d.switch_to_alert().dismiss()

# d.switch_to_frame("iframe-id")
# a = d.find_element_by_link_text(u"新增用户").click()
d.current_window_handle
a = d.find_element_by_id("iframe-id")
d.switch_to_frame(a)
# time.sleep(2)
num = 1
for i in range(1,5):
    s = int(random.uniform(2, 7))
    n = "qq%d"%num
    time.sleep(1)
    a = d.find_element_by_link_text(u"新增用户").click()
    d.find_element_by_name("user_name").send_keys(n)
    time.sleep(1)
    d.find_element_by_name("user_loginName").send_keys(n)
    time.sleep(1)
    d.find_element_by_name("user_password").send_keys("123456")
    time.sleep(1)
    d.find_element_by_name("user_type").find_elements_by_tag_name("option")[s].click()
    time.sleep(1)
    d.find_element_by_class_name("submitClick").click()
    num += 1

# d.close()
