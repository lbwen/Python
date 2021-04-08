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

data = ExcelR("ziyuan.xlsx")
ldata = data.dict_data()
@ddt.ddt
class Resources(unittest.TestCase):
    # def __init__(self):
    #     self.go_web = LoginTo()
    #     self.go_web.open_web()
    def setUp(self):
        print "开始"

    @ddt.data(*ldata)
    def test_login(self,ldata):

        self.aa.find_element_by_id("addBtn1").click()
        time.sleep(2)

        listName = ("id", "listName")
        listrank = ("id", "listrank")
        listCompanyName = ("id", "listCompanyName")
        listCompanyaddress = ("id", "listCompanyaddress")
        listPicture = ("id", "listPicture")
        audioListDetails1 = ("id", "audioListDetails1")
        listCompanyIntro = ("id", "listCompanyIntro")
        listcanOffer = ("id", "listcanOffer")

        WebDriverWait(self.aa, 10, 1).until(EC.presence_of_element_located(listName)).send_keys(ldata["name"])
        WebDriverWait(self.aa, 10, 1).until(EC.presence_of_element_located(listrank)).send_keys(ldata["touxian"])
        WebDriverWait(self.aa, 10, 1).until(EC.presence_of_element_located(listCompanyName)).send_keys(ldata["mingcheng"])
        WebDriverWait(self.aa, 10, 1).until(EC.presence_of_element_located(listCompanyaddress)).send_keys(ldata["dizhi"])
        WebDriverWait(self.aa, 10, 1).until(EC.presence_of_element_located(listPicture)).send_keys(ldata["shouyet"])
        WebDriverWait(self.aa, 10, 1).until(EC.presence_of_element_located(audioListDetails1)).send_keys(ldata["touxiasng"])
        WebDriverWait(self.aa, 10, 1).until(EC.presence_of_element_located(listCompanyIntro)).send_keys(ldata["jianjie"])
        WebDriverWait(self.aa, 10, 1).until(EC.presence_of_element_located(listcanOffer)).send_keys(ldata["tigong"])

        # 地区
        diqu = ldata["diqu"]
        Select(self.aa.find_element_by_id('listCity')).select_by_value(diqu)

        # 资源分类
        ziyuan = ldata["ziyuan"]
        Select(self.aa.find_element_by_id('listResources')).select_by_value(ziyuan)

        #行业分类
        fenlei = ldata["fenlei"]
        Select(self.aa.find_element_by_id('listClassification')).select_by_value(fenlei)

if __name__ == '__main__':
    unittest.main()