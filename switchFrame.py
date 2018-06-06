#encoding= utf-8
#通过Title属性识别弹出窗口P161-162
from selenium import webdriver
import unittest

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_HandleFrame(self):
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
        #使用索引方式进入指定frame页面，索引号从0开始
        #所以想进入中间的frame需要使用索引号1
        #如果没有使用此行代码则无法找到左边frame中的任何页面元素
        self.driver.switch_to.frame(0)
        leftframetext = self.driver.find_element_by_xpath("//p")
        print leftframetext.text
        #这里的断言用assertEqual也可以达到一样结果
        self.assertAlmostEqual(leftframetext.text,u"这是左侧frame页面上的文字")
        #找到左侧frame上的按钮，并单击该元素
        self.driver.find_element_by_tag_name("input").click()
        try:
            #动态等待alert窗口出现
            alertWindow=WebDriverWait(self.driver,10).until(EC.alert_is_present())
            #打印alert消息
            print alertWindow.text
            alertWindow.accept()
        except TimeoutException,e:
            print e
        #！！！switch_to.default_content方法，从左侧frame返回frameset页面
        #如果不调用此方法，则无法从左侧frame直接进入其他frame页面
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("frame")[1])
        assert u"这是中间frame页面上的文字" in self.driver.page_source
        self.driver.find_element_by_tag_name("input").send_keys(u"我在中间frame")
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.driver.find_element_by_id("rightframe"))
        assert u"这是右侧frame页面上的文字" in self.driver.page_source

        self.driver.switch_to.default_content()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
