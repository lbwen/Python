#coding:utf-8
from selenium import webdriver
class Dome():
    def get_open(self):
        self.driver = webdriver.Firefox()
        self.driver.get(r"http://dev.shidonghui.cn/sdhui/static/wr/newOam/index.html")

    def get_login(self):
        self.driver.find_element_by_id("uname").send_keys("admin")
        self.driver.find_element_by_id("upwd").send_keys("123456")
        self.driver.find_element_by_id("btn").click()

    def get_close(self):
        self.driver.close()

if __name__ == '__main__':
    demo = Dome()
    demo.get_open()
    demo.get_login()
    demo.get_close()