#encoding= utf-8
#操作ｗｅｂ页面的滚动条Ｐ１７３

from selenium import webdriver
import unittest
import traceback
from selenium.common.exceptions import WebDriverException
import time

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_executeScript(self):
        url="http://www.seleniumhq.org"
        try:
            self.driver.get(url)
            self.driver.execute_script("window.scrollTo(100,document.body.scrollHeight);")
            time.sleep(3)
            self.driver.execute_script("document.getElementById('choice').scrollIntoView(true);")
            time.sleep(3)
            self.driver.execute_script("window.scrollBy(0,400);")
            time.sleep(3)


        except Exception,e:
            print traceback.print_exc()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
