#encoding= utf-8
import HTMLTestRunner
from selenium import webdriver
import unittest, time

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://www.baidu.com"

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title=driver.title
        self.assertEqual(title, u"unittest_百度搜索")

    def test_baidu_set(self):
        driver=self.driver
        driver.get(self.base_url+"/gaoji/preferences.html")
        m=driver.find_element_by_name("NR")
        time.sleep(1)
        m.find_element_by_xpath("//option[@value='50']").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    testunit=unittest.TestSuite()

    testunit.addTest(BaiduTest("test_baidu_search"))
    testunit.addTest(BaiduTest("test_baidu_set"))

    filename= 'testtest.html'
    fp=open(filename,'wb')

    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test_title',description='result')
    runner.run(testunit)
    fp.close()

