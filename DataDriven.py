#encoding=utf-8
from selenium import webdriver
import unittest,time
import logging,traceback
import ddt
from ExcelUtil import ParseExcel
from selenium.common.exceptions import NoSuchElementException

#初始化日志对象
logging.basicConfig(
    level=logging.INFO,
    format= '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt = '%Y -%m - %d %H:%M:%S',
    filename=r'C:\Users\ali\PycharmProjects\ExcelDataDrivenProject\dataDrivenReport.log',
    filemode='w'
)

excelPath=r'B:\test\TestData.xlsx'
sheetName=u'test'
excel=ParseExcel(excelPath,sheetName)

@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    @ddt.data(* excel.getDataFromSheet())
    def test_dataDrivenByFile(self,data):
        testData,expectData=tuple(data)
        url='http://www.baidu.com'
        self.driver.get(url)
        self.driver.maximize_window()
        print testData,expectData
        try:
            self.driver.find_element_by_id("kw").send_keys(testData)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectData in self.driver.page_source)
        except NoSuchElementException,e:
            logging.error("the page doesnt exist")
        except Exception, e:
            logging.error("Unkonwn error")
        else:
            logging.info("search %s ,expected %s passed" %(testData,expectData))



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
     unittest.main()