#coding:utf-8
import unittest
import HTMLTestRunner

class Login(unittest.TestCase):
    def setUp(self):
        print "qqq"
    def test01(self):
        print "ddd"
    def test02(self):
        print "bbb"
    def test03(self):
        print "zzz"
    def test04(self):
        self.assertEqual(2,5,msg="qq")
    def tearDown(self):
        print "end"

if __name__=="__main__":
    unittest.main()