#encoding= utf-8
#通过模糊匹配选择悬浮框中的内容 P176
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback
import time


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_AjaxDivOptionByWords(self):
        url="http://www.sogou.com"
        self.driver.get(url)
        try:
            searchBox=self.driver.find_element_by_id("query")
            searchBox.send_keys("da")
            time.sleep(2)
            #find the matching by words ,if the result contains character link ,then click it,如果有多个匹配，选第一个
            suggestOptions=self.driver.find_element_by_xpath("//ul//li[contains(.,'西游')]")
            suggestOptions.click()
            time.sleep(3)

            self.driver.get(url)
            searchBox = self.driver.find_element_by_id("query")
            searchBox.send_keys("da")
            time.sleep(2)
            #如果只想选择固定第Ｎ项，可以参考一下代码，索引号从１开始，这里选第三个
            suggestOptions = self.driver.find_element_by_xpath("//*[@id='vl']/div[1]/ul/li[3]")
            suggestOptions.click()
            time.sleep(3)

        except NoSuchElementException,e:
            print traceback.print_exc()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
