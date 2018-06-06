#coding=utf-8
#浏览器中新开标签页Ｐ２１１
from selenium import webdriver
import unittest,time
import win32api,win32con

VK_CODE={'ctrl':0x11,'t':0x54,'tab':0x09}

def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName],0,0,0)
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName],0,win32con.KEYEVENTF_KEYUP,0)
def simulateKey(firstKey,secondKey):
    keyDown(firstKey)
    keyDown(secondKey)
    keyUp(secondKey)
    keyUp(firstKey)


class testDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_newTab(self):
        time.sleep(4)
        for i in range(2):
            simulateKey("ctrl","t")

        simulateKey("ctrl","tab")

        self.driver.get("http://www.sogou.com")
        self.driver.find_element_by_id("query").send_keys("test")
        self.driver.find_element_by_id("stb").click()
        time.sleep(3)

        all_handles=self.driver.window_handles
        print(len(all_handles))

        self.driver.switch_to.window(all_handles[1])
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("test")
        self.driver.find_element_by_id("su").click()
        time.sleep(4)

        self.driver.switch_to.window(all_handles[2])
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(4)
               




    def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
