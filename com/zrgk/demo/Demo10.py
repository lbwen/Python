#coding:utf-8
from selenium import webdriver
d = webdriver.Firefox()
d.get(r"http://169.254.5.87:8080/hospital")
# d.set_window_size(800,900)
d.title
# d.close()

import uniout
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox()
#等待4秒
driver.maximize_window()
driver.get(r"http://localhost:8080/jygl_houtai_ZLQ/login.jsp")
##通过name获取登录名并输入
username=driver.find_element_by_name("user_loginName").send_keys("xt")
##通过name获取密码并输入
pwd=driver.find_element_by_name("user_password").send_keys("123")
##找到要移动到下拉框位置
s1=driver.find_element_by_xpath("//li[@class='active']")
##移动
ActionChains(driver).move_to_element(s1).perform()
#选择系统管理
adm=driver.find_element_by_xpath("//li[contains(.,'系统管理员')]").click()
##登录
sub=driver.find_element_by_xpath("//button[@onclick='login()']").click()
##选择alert弹窗
alert=driver.switch_to_alert()
time.sleep(2)
##接受
alert.accept()

# btw=driver.find_element_by_class_name("active")

# # driver.close()
# btw.s
