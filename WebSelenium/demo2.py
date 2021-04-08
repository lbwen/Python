#coding:utf-8
import ddt
import time
import uniout
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_ziyuan import ExcelR
from login_to import LoginTo


@ddt.ddt
class Resources(unittest.TestCase):
    data = ExcelR("ziyuan.xlsx")
    ldata = data.dict_data()
    # def __init__(self):
    #     data = ExcelR("ziyuan.xlsx")
    #     ldata = data.dict_data()\
    @classmethod
    def setUpClass(self):
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

    @ddt.data(*ldata)
    def test_login(self,ldata):

        # for i in range(1,3):
        self.driver.find_element_by_id("addBtn1").click()
        time.sleep(2)

        listName = ("id", "listName")
        listrank = ("id", "listrank")
        listCompanyName = ("id", "listCompanyName")
        listCompanyaddress = ("id", "listCompanyaddress")
        listPicture = ("id", "listPicture")
        audioListDetails1 = ("id", "audioListDetails1")
        listCompanyIntro = ("id", "listCompanyIntro")
        listcanOffer = ("id", "listcanOffer")

        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(listName)).send_keys(ldata["name"])
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(listrank)).send_keys(ldata["touxian"])
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(listCompanyName)).send_keys(
            ldata["mingcheng"])
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(listCompanyaddress)).send_keys(
            ldata["dizhi"])
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(listPicture)).send_keys(ldata["shouyet"])
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(audioListDetails1)).send_keys(
            ldata["touxiasng"])
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(listCompanyIntro)).send_keys(
            ldata["jianjie"])
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(listcanOffer)).send_keys(ldata["tigong"])

        # 地区
        diqu = ldata["diqu"]
        Select(self.driver.find_element_by_id('listCity')).select_by_value(diqu)

        # 资源分类
        ziyuan = ldata["ziyuan"]
        Select(self.driver.find_element_by_id('listResources')).select_by_value(ziyuan)

        # 行业分类
        fenlei = ldata["fenlei"]
        Select(self.driver.find_element_by_id('listClassification')).select_by_value(fenlei)

        self.driver.find_element_by_id("saveBtn").click()
        time.sleep(3)

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()