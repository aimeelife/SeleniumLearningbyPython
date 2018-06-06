#encoding= utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest
import time

import win32clipboard as w
import win32con

#获取剪切板内容
def gettext():
   w.OpenClipboard()
   t = w.GetClipboardData(win32con.CF_TEXT)
   w.CloseClipboard()
   return t

#写入剪切板内容
def settext(aString):
   w.OpenClipboard()
   w.EmptyClipboard()
   w.SetClipboardData(win32con.CF_TEXT, aString)
   w.CloseClipboard()

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_copyAndPaste(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        content = "光荣之路"
        settext(content)
        getContent= gettext()
        print getContent
        print getContent.decode("gbk").encode("utf-8")
        self.driver.find_element_by_id("kw").click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(2)

        self.driver.find_element_by_id("su").click()
        time.sleep(3)


    def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()