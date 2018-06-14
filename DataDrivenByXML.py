#encoding=utf-8
from selenium import webdriver
import unittest,time,os
import logging,traceback
import ddt
from XmlUtil import ParseXML
from selenium.common.exceptions import NoSuchElementException

#初始化日志对象
logging.basicConfig(
    level=logging.INFO,
    format= '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt = '%Y -%m - %d %H:%M:%S',
    filename=r'C:\Users\ali\PycharmProjects\ExcelDataDrivenProject\dataDrivenReport.log',
    filemode='w'
)

currentPath=os.path.dirname(os.path.abspath(__file__))
dataFilePath=os.path.join(currentPath,'TestDataXML.xml')
print dataFilePath

xml=ParseXML(dataFilePath)

@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    @ddt.data(* xml.getDataFromXML())
    def test_dataDrivenByXML(self,data):
        testData,expectData=data["name"],data["author"]
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
        except AssertionError,e:
            logging.info("search '%s' ,expected '%s' , failed " %(testData,expectData))
        except Exception, e:
            logging.error("Unkonwn error")
        else:
            logging.info("search %s ,expected %s passed" %(testData,expectData))



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
     unittest.main()