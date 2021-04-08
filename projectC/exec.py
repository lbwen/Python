#-*- coding:utf-8 -*-
import unittest
import os
def all_case():    #执行测试用例的目录
 cur_path = os.path.dirname(os.path.realpath(__file__))
 caseName = "case"
 case_path = os.path.join(cur_path, caseName)
# case_dir = r"D:\se\projectC\case"
 testcase = unittest.TestSuite()
 dis=unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
 return dis
if __name__=="__main__":    #返回实例
   runner = unittest.TextTestRunner()    #run所有用例
   runner.run(all_case())



