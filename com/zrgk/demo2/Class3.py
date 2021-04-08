#coding:utf-8
import unittest
import HTMLTestRunner

class AA(unittest.TestCase):
    def setUp(self):
        pass
    def test01(self):
        self.assertEqual(4,6,msg="aa")
    def test02(self):
        self.assertEqual(5,5)
    def test03(self):
        self.assertIn("a","cvb")
    def test04(self):
        self.assertIn("z","zxc")

if __name__=="__main__":
    rongqi = unittest.TestSuite()
    rongqi.addTest(AA("test01"))
    rongqi.addTest(AA("test02"))
    rongqi.addTest(AA("test03"))
    rongqi.addTest(AA("test04"))
    url = "csbg.html"
    fp = file(url,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,title=u"报告",description="reort"
    )
    runner.run(rongqi)