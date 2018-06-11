#encoding=utf-8
from selenium import webdriver
import unittest
import time
from table import Table

class TestTableOperation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testTable(self):
        url="https://d-applications2013.icao.lan/eHRAP"
        self.driver.get(url)
        #获取被测试网页中的table元素存在webTable变量中
        webTable=self.driver.find_element_by_tag_name("table")
        #使用WebTable对Table类实例化
        table=Table(webTable)
        #统计表格的行列数
        print table.getRowCount()
        print table.getColumnCount()

        cell=table.getCell(3,1)
        print cell.text
''' 
#获取表格第三行第二列中的输入框对象，并输入“第三行第二列表格被找到”
        cellInput=table.getWebElementInCell(3,2,"tag name","input")
        cellInput.send_keys(u"第三行第二列表格被找到")

'''
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()