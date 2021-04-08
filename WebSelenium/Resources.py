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

data = ExcelR("ziyuan.xlsx")
ldata = data.dict_data()
@ddt.ddt
class Resources(unittest.TestCase):
    def setUp(self):
        print "开始"

    @ddt.data(*ldata)
    def test_login(self,ldata):
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
        # for i in range(1,3):
        driver.find_element_by_id("addBtn1").click()
        time.sleep(2)

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

        # 行业分类
        fenlei = ldata["fenlei"]
        Select(driver.find_element_by_id('listClassification')).select_by_value(fenlei)

        driver.find_element_by_id("saveBtn").click()
        time.sleep(5)
        driver.close()

    def tearDown(self):
        print "完成"


if __name__ == '__main__':
    unittest.main()