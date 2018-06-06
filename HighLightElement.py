#coding=utf-8
#高亮显示正在操作的元素Ｐ２１０
from selenium import webdriver
import unittest,time

def highLightElement(driver,element):
    #driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,"background:green, border:3px solid red;")
    #原始栗子里修改了两个attribute,run起来看不见变动，改成高亮任意一个Attribute都可以显示
    driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,"border:3px solid red;")


class testDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_highLightElement(self):
        url="http://www.sogou.com"
        self.driver.get(url)
        searchBox=self.driver.find_element_by_id("query")
        highLightElement(self.driver,searchBox)
        time.sleep(30)
        searchBox.send_keys("test")
        submitButton=self.driver.find_element_by_id("stb")
        highLightElement(self.driver,submitButton)
        time.sleep(5)
        submitButton.click()
        time.sleep(5)


    def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
