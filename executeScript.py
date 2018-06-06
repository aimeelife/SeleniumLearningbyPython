#encoding= utf-8
#使用JAVAScript操作页面元素
from selenium import webdriver
import unittest
import traceback
from selenium.common.exceptions import WebDriverException
import time

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_executeScript(self):
        url="http://www.baidu.com"
        self.driver.get(url)

        searchInputBoxJS="document.getElementById('kw').value='光荣之路'"
        searchBottonJS = "document.getElementById('su').click()"
        try:
            self.driver.execute_script(searchInputBoxJS)
            time.sleep(2)
            self.driver.execute_script(searchBottonJS)
            time.sleep(2)
            self.assertTrue(u"百度百科" in self.driver.page_source)
        except WebDriverException,e:
            print traceback.print_exc()
        except AssertionError,e:
            print "page doesnt exist"
        except Exception,e:
            print traceback.print_exc()
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
