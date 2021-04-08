#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BaseC():
    def __init__(self,driver):
        self.driver=driver
    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    # def find_element(self,locator):
    #     element=WebDriverWait(self.driver,20).until(EC.presence_of_element_located(locator))
    #     return element
    def find_element(self, locator, timeout=10):
        '''定位元素，参数locator是元祖类型'''
        #("id","kw"
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return element
    def send_keys(self,locator,text,is_clear=True):
        element = self.find_element(locator)
        if is_clear == True: element.clear()
        element.send_keys(text)
    def click(self,locator):
        element = self.find_element(locator)
        element.click()
    # def clear(self,locator):
    #     self.find_element(locator).clear()
    def is_ele_text(self,locator,text):
        re=WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(locator,text))
        return re#true he false
    def is_ele_value(self,locator,text):
        re=WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element_value(locator,text))
        return re#true he false
    def is_title(self,title):
        re = WebDriverWait(self.driver,20).until(EC.title_is(title))
        return re  # true he false
    def is_alert(self):
        re = WebDriverWait(self.driver,20).until(EC.alert_is_present())
        return re  # true he false
    def is_text_in_element(self, locator, text, timeout=10):
        '''
        判断文本在元素里,没定位到元素返回False，定位到返回判断结果布尔值
        result = driver.text_in_element(locator, text)
        '''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
        return result
    def get_text(self, locator):
        '''获取文本'''
        t = self.find_element(locator).text
        return t
#if __name__=="__main__":
    # driver = webdriver.Firefox()
    # driver.get("https://www.baidu.com ")
    # d=BaseC(driver)
    # lacator = ("id", "kw")#定位元素
    # d.send_keys(lacator,"selenium")
    # d.click(lacator)
    # #d.send_keys(lacator,u"百度")
    # #d.click(lacator)
    # re=d.is_title(u"selenium_百度搜索")
    # print re


