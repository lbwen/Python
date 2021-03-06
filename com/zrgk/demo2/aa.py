# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import xlrd

class Aa(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_aa(self):
        driver = self.driver
        driver.get(self.base_url + "/zentao/user-login-L3plbnRhby8=.html")
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_link_text(u"组织").click()
        driver.find_element_by_link_text(u"添加用户").click()
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("ee")
        driver.find_element_by_id("realname").clear()
        driver.find_element_by_id("realname").send_keys("dd")
        driver.find_element_by_id("password1").clear()
        driver.find_element_by_id("password1").send_keys("123")
        driver.find_element_by_id("password2").clear()
        driver.find_element_by_id("password2").send_keys("123")
        driver.find_element_by_id("verifyPassword").clear()
        driver.find_element_by_id("verifyPassword").send_keys("123456")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_css_selector("body.m-user-create").click()
        driver.find_element_by_id("password1").clear()
        driver.find_element_by_id("password1").send_keys("123123")
        driver.find_element_by_id("password2").clear()
        driver.find_element_by_id("password2").send_keys("123123")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_css_selector("body.m-user-create").click()
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("eee")
        driver.find_element_by_id("submit").click()
    
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

if __name__ == "__main__":
    unittest.main()
