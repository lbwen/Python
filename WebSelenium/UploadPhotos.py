#coding=utf-8
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Upload_Photos:
    def photos(self):
        driver = webdriver.Firefox()
        driver.maximize_window()  # 最大化浏览器窗口
        driver.get(r"http://dev.shidonghui.cn/sdhui/static/wr/newOam/login.html")
        time.sleep(2)

        driver.find_element_by_id("uname").send_keys("admin")
        driver.find_element_by_id("upwd").send_keys("123456")
        driver.find_element_by_id("btn").click()
        time.sleep(2)

        ResourceList = driver.find_elements_by_xpath("//div[@class = 'text-center']")
        ResourceList[34].click()
        time.sleep(2)
        driver.find_element_by_link_text("清单列表").click()
        driver.find_element_by_id("addBtn1").click()
        time.sleep(2)

        #上传头像
        # driver.find_element_by_id("upAudioListDetailsBtn1").click()
        # os.system("E:\autoit\创建文件\Head.exe")

        #上传首页图
        driver.find_element_by_id("upLoadAudioBtn").click()
        # driver.find_element_by_xpath("//*[@class = 'btn btn-info']").click()
        # driver.find_element_by_css_selector("[class='btn btn-info']").click()
        #选择图片
        # m = driver.find_element_by_xpath("//*[@class = 'btn btn-info']")
        # ActionChains(driver).move_to_element(m).perform()
        #确认上传   upLoadImageBtn
        # m = driver.find_element_by_xpath("//*[@type='button']")
        # ActionChains(driver).move_to_element(m).perform()

        #点击X
        m = driver.find_element_by_xpath("//button[@type='button']")
        ActionChains(driver).move_to_element(m).perform()


if __name__ == '__main__':
    upLoad = Upload_Photos()
    upLoad.photos()
