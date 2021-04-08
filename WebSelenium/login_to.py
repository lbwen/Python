#coding:utf-8
import time
import uniout
from selenium import webdriver

class LoginTo:
    def open_web(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()  # 最大化浏览器窗口
        self.driver.get(r"http://dev.shidonghui.cn/sdhui/static/wr/newOam/login.html")
        time.sleep(2)

        self.driver.find_element_by_id("uname").send_keys("admin")
        self.driver.find_element_by_id("upwd").send_keys("123456")
        self.driver.find_element_by_id("btn").click()
        time.sleep(2)

        ResourceList = self.driver.find_elements_by_xpath("//div[@class = 'text-center']")
        ResourceList[34].click()
        time.sleep(2)
        self.driver.find_element_by_link_text("清单列表").click()
        return self.driver

    def close_web(self):
        self.driver.close()

# if __name__ == '__main__':
#     login = LoginTo()
#     login.open_web()
#     login.close_web()
