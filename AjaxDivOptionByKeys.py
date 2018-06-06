#encoding= utf-8
#模拟键盘下箭头进行悬浮框选项选择　Ｐ１７５
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time


class SetPageLoadTime(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_AjaxDivOptionByKeys(self):
        url="http://www.sogou.com"
        self.driver.get(url)
        searchBox=self.driver.find_element_by_id("query")
        searchBox.send_keys("test")
        time.sleep(2)
        for i in range(3):
            searchBox.send_keys(Keys.DOWN)
            time.sleep(0.5)
        searchBox.send_keys(Keys.ENTER)
        time.sleep(3)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
