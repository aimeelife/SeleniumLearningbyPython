#encoding=utf-8

class Table(object):
    #定义一个私有属性__table,用于存放table对象
    __table=''

    def __init__(self,table):
        self.setTable(table)

    def setTable(self,table):
        self.__table=table

    def getTable(self):
        return self.__table

    def getRowCount(self):
        return len(self.__table.find_elements_by_tag_name("tr"))

    def getColumnCount(self):
        return len(self.__table.find_elements_by_tag_name("tr")[0].find_elements_by_tag_name("td"))

    def getCell(self,rowNo,colNo):
        try:
            currentRow=self.__table.find_elements_by_tag_name("tr")[rowNo-1]
            currentCol=currentRow.find_elements_by_tag_name("td")[colNo-1]
            return currentCol
        except Exception,e:
            raise e

    def getWebElementInCell(self,rowNo,colNo,by,value):
        try:
            currentRow = self.__table.find_elements_by_tag_name("tr")[rowNo - 1]
            currentCol = currentRow.find_elements_by_tag_name("td")[colNo - 1]
            element=currentCol.find_Element(by=by,value=value)
            return element
        except Exception,e:
            raise e
