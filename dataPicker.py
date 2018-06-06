#encoding= utf-8
#更改一个页面对象的属性值Ｐ１７９　
#针对页面元素属性的增删改都是临时的，只针对当前会话有效，源码并没有真正被修改
from selenium import webdriver
import unittest

def addAttribue(driver,elementObj,attributeName,value):
    driver.execute_script("arguments[0].%s=arguments[1]"%attributeName,elementObj,value)

def setAttribue(driver,elementObj,attributeName,value):
    driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",elementObj,attributeName,value)

def getAttribue(elementObj,attributeName):
    return elementObj.get_attribute(attributeName)

def removeAttribue(driver,elementObj,attributeName):
    driver.execute_script("arguments[0].removeAttribute(arguments[1])",elementObj,attributeName)


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_dataPicker(self):
        url=r"C:/Users/ali/PycharmProjects/UnitTestProj/operateAttribute.html"
        self.driver.get(url)
        element=self.driver.find_element_by_xpath("//input")
        addAttribue(self.driver,element,'name','search')
        print getAttribue(element,"name")
        print getAttribue(element,"value")
        print getAttribue(element,"size")

        setAttribue(self.driver,element,"size",100)
        print getAttribue(element, "size")
        setAttribue(self.driver, element, "value", "改啦改啦")
        print getAttribue(element, "value")

        removeAttribue(self.driver,element,"value")
        print "get attribute value after delete it:", getAttribue(element, "value")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
