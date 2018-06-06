#encoding= utf-8
#p140
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import unittest

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_simulationCombinationKeys(self):
        url="http://www.baidu.com"
        self.driver.get(url)
        input = self.driver.find_element_by_id("kw")
        input.click()
        input.send_keys("test")
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()

        self.driver.get(url)
        self.driver.find_element_by_id("kw").click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        self.driver.find_element_by_id("su").click()
        time.sleep(3)

    def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()