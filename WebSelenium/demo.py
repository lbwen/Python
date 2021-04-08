#coding:utf-8
import ddt
import time
import uniout
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from read_ziyuan import ExcelR

data = ExcelR("ziyuan.xlsx")
ldata = data.dict_data()
@ddt.ddt
class Resources(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()  # 最大化浏览器窗口
        # self.base_url = "http://dev.shidonghui.cn/sdhui/static/wr/newOam/login.html"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get(r"http://dev.shidonghui.cn/sdhui/static/wr/newOam/login.html")
        self.driver.find_element_by_id("uname").send_keys("admin")
        self.driver.find_element_by_id("upwd").send_keys("123456")
        self.driver.find_element_by_id("btn").click()
        time.sleep(2)
        ResourceList = self.driver.find_elements_by_xpath("//div[@class = 'text-center']")
        ResourceList[34].click()
        time.sleep(2)
        self.driver.find_element_by_link_text("清单列表").click()
        self.driver.find_element_by_id("addBtn1").click()
        time.sleep(2)

    @ddt.data(*ldata)
    def test_login(self,ldata):
        driver = self.driver
        listName = ("id", "listName")
        listrank = ("id", "listrank")
        listCompanyName = ("id", "listCompanyName")
        listCompanyaddress = ("id", "listCompanyaddress")
        listPicture = ("id", "listPicture")
        audioListDetails1 = ("id", "audioListDetails1")
        listCompanyIntro = ("id", "listCompanyIntro")
        listcanOffer = ("id", "listcanOffer")

        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(listName)).send_keys(ldata["name"])
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(listrank)).send_keys(ldata["touxian"])
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(listCompanyName)).send_keys(ldata["mingcheng"])
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(listCompanyaddress)).send_keys(ldata["dizhi"])
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(listPicture)).send_keys(ldata["shouyet"])
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(audioListDetails1)).send_keys(ldata["touxiasng"])
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(listCompanyIntro)).send_keys(ldata["jianjie"])
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(listcanOffer)).send_keys(ldata["tigong"])

        # 地区
        diqu = ldata["diqu"]
        Select(driver.find_element_by_id('listCity')).select_by_value(diqu)

        # 资源分类
        ziyuan = ldata["ziyuan"]
        Select(driver.find_element_by_id('listResources')).select_by_value(ziyuan)

        #行业分类
        fenlei = ldata["fenlei"]
        Select(driver.find_element_by_id('listClassification')).select_by_value(fenlei)

        #保存
        driver.find_element_by_id("saveBtn").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text

            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()