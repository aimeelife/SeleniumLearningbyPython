#coding=utf-8
from selenium import webdriver
import unittest,time

class TestDemo(unittest.TestCase):
    def setUp(self):
        #实例化一个火狐配置文件
        fp = webdriver.FirefoxProfile()
        #设置各项参数，参数可以通过在浏览器地址栏中输入about:config查看。
        #下载到指定目录
        fp.set_preference("browser.download.dir","b:\\test")
        #设置成0代表下载到桌面，1表示浏览器默认下载路径；设置成2则可以保存到指定目录
        fp.set_preference("browser.download.folderList",2)
        #让用户处理，默认TRUE，设定成False，表示不会记录打开未知MIME类型
        fp.set_preference("browser.helperApps.alwaysAsk.force", False)
        #是否显示开始下载管理器,(个人实验，不管设成True还是False，都不显示开始，直接下载)
        fp.set_preference("browser.download.manager.showWhenStarting",False)
        # 是否隐藏下拉框，False表示隐藏
        fp.set_preference("browser.download.manager.useWindow", False)
        fp.set_preference("browser.download.manager.focusWhenStarting", False)
        fp.set_preference("browser.download.manager.alertOnEXEOpen", False)



        #不询问下载路径；后面的参数为要下载页面的Content-type的值
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip,application/octet-stream")
        fp.set_preference("browser.helperApps.neverAsk.showAlertOnComplete",False)
        fp.set_preference("browser.helperApps.neverAsk.closeWhenDone", False)


        #启动一个火狐浏览器进程，以刚才的浏览器参数
        self.driver = webdriver.Firefox(firefox_profile=fp)

    def test_dataDownload(self):
        #打开下载页面
        url="https://github.com/mozilla/geckodriver/releases"
        self.driver.get(url)
        self.driver.find_element_by_xpath("//strong[.='geckodriver-v0.20.1-win64.zip']").click()
        time.sleep(10)

        url1="https://www.python.org/download/releases/2.7.1/"
        self.driver.get(url1)
        self.driver.find_element_by_link_text("Windows X86-64 MSI Installer (2.7.1)").click()
        time.sleep(100)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
