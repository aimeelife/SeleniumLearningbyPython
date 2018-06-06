#encoding= utf-8
from selenium import webdriver
import unittest

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_getBaicInfo(self):
        url="https://www.baidu.com"
        self.driver.get(url)
      #  newElement =self.driver.find_element_by_css_selector('.mnav')
        newElement = self.driver.find_element_by_xpath('//a[.="新闻"]')

        print newElement.get_attribute('name')

        print (newElement.tag_name)
        print newElement.text
        print newElement.size

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
