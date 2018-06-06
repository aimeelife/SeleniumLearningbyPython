#encoding= utf-8
#操作javascript的alert弹框P165
from selenium import webdriver
import unittest

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Cookie(self):
        url="http://www.sogou.com"
        self.driver.get(url)
        cookies=self.driver.get_cookies()
        print cookies
        for cookie in cookies:
            print "%s->%s->%s->%s->%s"%(cookie['domain'],cookie['name'],cookie['value'],cookie['expiry'],cookie['path'])

        ck=self.driver.get_cookie("SUV")
        print "%s->%s->%s->%s->%s" % (ck['domain'], ck['name'], ck['value'], ck['expiry'], ck['path'])
        self.driver.delete_cookie("ABTEST")
        cookies=self.driver.get_cookies()
        print cookies

        self.driver.delete_all_cookies()
        print "delete all cookies"
        cookies = self.driver.get_cookies()
        print cookies

        self.driver.add_cookie({"name":"testaddcookie","value":"123456789"})
        print 'new cookie added'
        cookie =self.driver.get_cookie("testaddcookie")
        print cookie


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
