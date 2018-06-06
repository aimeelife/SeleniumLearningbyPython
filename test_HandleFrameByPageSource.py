#encoding= utf-8
#通过html源码内容操作frame P163
from selenium import webdriver
import unittest

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_HandleFrameByPageSource(self):
        #导入多个异常类型
        from selenium.common.exceptions import NoSuchWindowException,TimeoutException
        #导入期望场景类
        from selenium.webdriver.support import expected_conditions as EC
        # 导入堆栈类
        import traceback
        # 导入BY类
        from selenium.webdriver.common.by import By
        # 导入显式等待类
        from selenium.webdriver.support.ui import WebDriverWait
        #导入时间模块
        import time
        url=r"C:/Users/ali/PycharmProjects/UnitTestProj/frameset.html"
        #访问自动已测试网页
        self.driver.get(url)
        frameList =self.driver.find_elements_by_tag_name("frame")
        for frame in frameList:
            self.driver.switch_to.frame(frame)

            if u"中间frame" in self.driver.page_source:
                p=self.driver.find_element_by_xpath("//p")
                self.assertAlmostEqual(p.text, u"这是中间frame页面上的文字")
                self.driver.switch_to.default_content()
                break
            else:
                self.driver.switch_to.default_content()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
