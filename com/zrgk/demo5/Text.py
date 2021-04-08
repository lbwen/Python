#coding:utf-8
import uniout
import ddt
import unittest
from selenium import webdriver
import HTMLTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from com.zrgk.demo4.Demo1 import ExcelR
from com.zrgk.demo2.Class5 import all_case
# data = [{"name":"admin","pwd":"123456"}]
data = ExcelR("text.xlsx")
ldata = data.dict_data()

@ddt.ddt
class Tandao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(r"http://localhost/zentao/")
        self.driver.implicitly_wait(10)
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Firefox()
    #     cls.driver.get(r"http://localhost/zentao/")
    #     cls.driver.implicitly_wait(10)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

    @ddt.data(*ldata)
    def testLogin(self,ldata):
        username = ("xpath","//input[@id='account']")
        password = ("name","password")
        submit = ("id","submit")
        loginout = ("link text", u"退出")


        # WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(username)).send_keys("admin")
        # WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(password)).send_keys("123456")
        # WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(submit)).click()

        # WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(username)).send_keys(ldata["name"])
        # WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(password)).send_keys(ldata["pwd"])
        # WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(submit)).click()

        WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(username)).send_keys(ldata["name"])
        WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(password)).send_keys(ldata["pwd"])
        WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(submit)).click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(loginout)).click()


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()




