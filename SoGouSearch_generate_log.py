#encoding=utf-8
from selenium import webdriver
import unittest
from Log import *

'''
Log会写入b:\\test\AutoTestLog.log　文件中，每次结果都写入同一个ｌｏｇ文件

'''
class TestSoGouSearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()

    def testSoGouSearch(self):
        info(u"===================搜索===================")
        url="http://www.sogou.com"
        self.driver.get(url)
        info(u"访问sogou首页")
        self.driver.find_element_by_id("query").send_keys("test")
        info(u"在输入框输入test")
        self.driver.find_element_by_id("stb").click()
        info(u"单击搜索按钮")
        info(u"===================测试用例执行结束===================")



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
        unittest.main()