#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get(r"http://localhost/zentao/")
driver.implicitly_wait(10)

username = ("xpath","//input[@id='account']")
password = ("name","password")
submit = ("id","submit")
loginout = ("link text",u"退出")

WebDriverWait(driver,10,1).until(EC.presence_of_element_located(username)).send_keys("admin")
WebDriverWait(driver,10,1).until(EC.presence_of_element_located(password)).send_keys("123456")
WebDriverWait(driver,10,1).until(EC.presence_of_element_located(submit)).click()
WebDriverWait(driver,10,1).until(EC.presence_of_element_located(loginout)).click()


# driver.find_element_by_link_text(u"退出").click()
