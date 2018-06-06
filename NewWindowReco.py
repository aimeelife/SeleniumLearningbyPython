#encoding= utf-8
#通过Title属性识别弹出窗口P159
from selenium import webdriver
import unittest

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_identifyPopUpWindowByTitle(self):
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
        url=r"C:/Users/ali/PycharmProjects/UnitTestProj/test.html"
        #访问自动已测试网页
        self.driver.get(url)
        #显式等待找到页面上链接文字为sogou搜索的连接元素，找到后单击它
        WebDriverWait(self.driver,10,0.2).until(EC.element_to_be_clickable((By.LINK_TEXT,"sogou搜索"))).click()
        #获取当前所有打开的浏览器窗口句柄
        all_handles=self.driver.window_handles
        #打印当前打开的浏览器窗口句柄
        print self.driver.current_window_handle
        print all_handles
        #打印打开的浏览器窗口个数
        print len(all_handles)
        time.sleep(2)
        #如果存储浏览器窗口句柄的容器不为空，再历遍all_handles中所有的浏览器句柄
        if len(all_handles)>0:
            try:
                for windowHandle in all_handles:
                    #切换窗口
                    self.driver.switch_to.window(windowHandle)
                    print self.driver.title
                    #判断当前浏览器窗口的title属性是否等于下句
                    if self.driver.title == u"搜狗搜索引擎 - 上网从搜狗开始":
                        #显式等待页面搜索输入框加载完成，然后输入sogou首页窗口被找到
                        WebDriverWait(self.driver,10,0.2).until(lambda x: x.find_element_by_id("query")).send_keys(u"sogou首页窗口被找到")
                        print u"find sogou"
                        time.sleep(2)
            except NoSuchWindowException,e:
                #捕获异常
                print traceback.print_exc()
            except TimeoutException, e:
                #捕获异常
                print traceback.print_exc()
        #把窗口切换回默认窗口
        self.driver.switch_to.window(all_handles[0])
        print self.driver.title
        #断言当前浏览器窗口title属性是“你喜欢的水果”
        self.assertEqual(self.driver.title,u"你喜欢的水果")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
