#coding:utf-8
import uniout
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
# driver.get(r"http://169.254.37.125/zentao/user-login.html")
# time.sleep(5)
# driver.find_element_by_name("account").send_keys("admin")
# driver.find_element_by_name("password").send_keys("123456")
# driver.find_element_by_id("submit").click()

driver.get(r"https://www.baidu.com/")
time.sleep(5)
# driver.find_element_by_partial_link_text("推广").click()
mm = driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(mm).perform()

# driver.close()

