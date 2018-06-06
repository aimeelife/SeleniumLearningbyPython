import unittest
from selenium import webdriver
import time

class GloryRoad(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def testSoGou(self):
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element_by_id("query").clear()
        self.driver.find_element_by_id("query").send_keys(u"WebDriver")
        self.driver.find_element_by_id("stb").click()
        time.sleep(3)
        assert u"Java" in self.driver.page_source, "not in keyword"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
