#encoding= utf-8
#操作ｉｆｒａｍｅ中的页面元素Ｐ１６４
from selenium import webdriver
import unittest

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_HandleIFrame(self):
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
        self.driver.switch_to.frame(0)
        assert u"这是左侧frame页面上的文字" in self.driver.page_source

        self.driver.switch_to.frame(self.driver.find_element_by_id("showIframe"))
        assert u"这是iframe页面上的文字" in self.driver.page_source

        self.driver.switch_to.default_content()
        assert u"frameset页面" in self.driver.page_source

        self.driver.switch_to.frame(1)
        assert u"这是中间frame页面上的文字" in self.driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
