#encoding=utf-8
from selenium import webdriver
import unittest,time,os
from FileUtil import createDir
import traceback

'''
创建存放异常截图的目录，并得到本次实例中存放目录的绝对路径
并作为全局变量，供本次所有测试用例调用
'''
picDir=createDir()

def takeScreenShot(driver,savePath,picName):
    #封装截屏方法
    #构造屏幕截图路径及图片名
    picPath=os.path.join(savePath,str(picName).decode("utf-8").encode("gbk")+".png")
    try:
        driver.get_screenshot_as_file(picPath)
    except Exception,e:
        print traceback.print_exc()

class TestFailCaptureScreen(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()

    def test_SoGouSearch(self):
        url="http://www.sogou.com"
        self.driver.get(url)
        try:
            self.driver.find_element_by_id("query").send_keys("test")
            self.driver.find_element_by_id("stb").click()
            time.sleep(3)
            self.assertTrue(u"shizairenwei" in self.driver.page_source,"doesn't find shizairenwei")
        except AssertionError,e:
            #调用封装好的截图方法，进行截图并保存在本地磁盘
            takeScreenShot(self.driver,picDir,e)
        except Exception,e:
            print traceback.print_exc()
            takeScreenShot(self.driver,picDir,e)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
        unittest.main()