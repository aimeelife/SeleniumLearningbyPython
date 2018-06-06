#encoding= utf-8
#操作javascript的alert弹框P165
from selenium import webdriver
import unittest

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_HandleIFrame(self):
        #导入Alert异常类型
        from selenium.common.exceptions import NoAlertPresentException
        #导入时间模块
        import time
        url=r"C:/Users/ali/PycharmProjects/UnitTestProj/alert.html"
        #访问自动已测试网页
        self.driver.get(url)
        button =self.driver.find_element_by_id("button")
        button.click()

        try:
            #动态等待alert窗口出现
            alert=self.driver.switch_to.alert
            time.sleep(2)
            self.assertAlmostEqual(alert.text, u"这是一个alert弹出框")
            alert.accept()

        except NoAlertPresentException,e:
            self.fail(u"尝试操作的alert框未被找到")
            print e

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
