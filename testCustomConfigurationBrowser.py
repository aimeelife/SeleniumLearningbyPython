#coding=utf-8
from selenium import webdriver
import unittest,time
from selenium.common.exceptions import NoSuchElementException

class testCustomConfigurationBrowser(unittest.TestCase):
    def setUp(self):
        proPath=r"C:\Users\ali\AppData\Local\Mozilla\Firefox\Profiles\to3e7ksd.WebDriver"
        #加载自定义配置文件到ｆｉｒｅｆｏｘ中
        profile=webdriver.firefox.firefox_profile.FirefoxProfile(proPath)
        profile.set_preference("browser.startup.homepage","http://www.sogou.com")
        profile.set_preference("browser.startup.page",1)
        self.driver = webdriver.Firefox(firefox_profile=profile)

    def testSoGouSearch(self):
        time.sleep(5)
        try:
            searchBox= self.driver.find_element_by_id("query")
            searchBox.send_keys("test")
            self.driver.find_element_by_id("stb").click()
            time.sleep(10)
        except NoSuchElementException,e:
            print "doesn't work"

    def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
