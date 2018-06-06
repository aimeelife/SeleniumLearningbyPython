#encoding= utf-8
#指定页面加载时间P170
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time


class SetPageLoadTime(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_PageLoadTime(self):
        self.driver.set_page_load_timeout(15)
        self.driver.maximize_window()
        try:
            startTime = time.time()
            self.driver.get("http://mail.126.com")
        except TimeoutException:
            print "time out"
            self.driver.execute_script("window.stop()")
        end=time.time()-startTime
        print end

        self.driver.switch_to.frame("x-URS-iframe")
        userName=self.driver.find_element_by_xpath("//input[@name='email']")
        value=userName.get_attribute("value")
        print value
        userName.send_keys("xxx")
        pwd = self.driver.find_element_by_xpath("//input[@name='password']")
        pwd.send_keys("xxx")
        pwd.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
