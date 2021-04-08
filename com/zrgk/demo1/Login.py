#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
d = webdriver.Firefox()
d.get(r"http://localhost:8080/jygl_houtai_ZLQ/login.jsp")
d.find_element_by_name("user_loginName").send_keys("xt")
d.find_element_by_name("user_password").send_keys("123")
m = d.find_element_by_xpath("//li[@class='active']")
ActionChains(d).move_to_element(m).perform()
d.find_element_by_xpath("//li[contains(.,'系统管理员')]").click()
d.find_element_by_xpath("//button[@onclick = 'login()']").click()
#点击弹窗的确定
d.switch_to_alert().accept()
#点击弹窗的取消
# d.switch_to_alert().dismiss()



# d.close()
