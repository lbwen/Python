#coding:utf-8
import unittest
import HTMLTestRunner
class GG(unittest.TestCase):
    # def setUp(self):
    #     print "starting"
    # def tearDown(self):
    #     print "ending"
    @classmethod
    def setUpClass(cls):
        print "starting"

    @classmethod
    def tearDownClass(cls):
        print "ending"

    def test01(self):
        print "qqq"
    def test02(self):
        print "aaa"
    def test03(self):
        print "zzz"
    def test04(self):
        try:
            self.assertEqual(2,5,msg="qq")
        except:
            print "bbb"

if __name__=="__main__":
    unittest.main()
