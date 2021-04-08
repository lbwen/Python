#coding:utf-8
import uniout
import unittest
import HTMLTestRunner
import threading
import time
from appium import webdriver
from AppiumPython1.bussiness.login_business import LoninBusiness
# class ParmeTestCase(unittest.TestCase):
#     def __init__(self,methodName='runTest',parame=None):
#         super(ParmeTestCase,self).__init__(methodName)
#         self.parame = parame

class CaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "setUpclass------>"
        # cls.login_business = LoninBusiness(i)
    def setUp(self):
        print "this is setUp\n"
    def test_01(self):
        # print "test case 里面的参数", self.parame
        # self.login_business.login_pass()

        # print "这是测试方法里面的："

        flag = True
        # self.assertEqual(1,2,u"数据错误")
        self.assertNotEqual(1,1,"数据错误")
        # self.assertTrue(flag,"数据错误")
        # self.assertFalse(flag,"fige")
    # @unittest.skip("CaseTest")
    def test_02(self):
        print "this is case02"
        self.assertNotEqual(1, 1, msg="数据错误")
    def tearDown(self):
        print "this is tearDown"
    @classmethod
    def tearDownClass(cls):
        print "this is class tearDown"

def get_suite(i):
    suite = unittest.TestSuite()
    # suite.addTest(CaseTest("test_02"))
    suite.addTest(CaseTest("test_01"))
    # unittest.TextTestRunner().run(suite)
    html_file = "E:/python/word/AppiumPython1/report/report"+str(i)+".html"
    fp = file(html_file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp, title=u"报告", description="reort"
    )
    runner.run(suite)

if __name__ == '__main__':
    # unittest.main()
    threads = []
    for i in range(3):
        # print i
        t = threading.Thread(target=get_suite,args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
