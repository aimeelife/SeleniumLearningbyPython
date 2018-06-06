#encoding= utf-8
from selenium import webdriver
import unittest

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_captureScreen(self):
        url="http://www.sogou.com"
        self.driver.get(url)
        try:
            result=self.driver.get_screenshot_as_file(r"b:\screenPicture.png")
            print result
        except IOError,e:
            print e



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()