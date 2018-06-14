#encoding=utf-8
from xml.etree import ElementTree

class ParseXML(object):
    def __init__(self,xmlPath):
        self.xmlPath=xmlPath

    def getRoot(self):
        tree=ElementTree.parse(self.xmlPath)
        return tree.getroot()

    def findNodeByName(self,parentNode,nodeName):
        nodes=parentNode.findall(nodeName)
        return nodes

    def getNodeOfChildText(self,node):
        childrenTextDict={i.tag:i.text for i in list(node.iter())[1:]}
        #上面的代码等价于下面的代码
        '''
        childrenTextDict={}
        for i in list(node.iter())[1:]:
            childrenTextDict[i.tag]=i.text
        '''
        return childrenTextDict

    def getDataFromXML(self):
        root=self.getRoot()
        books=self.findNodeByName(root,"book")
        dataList=[]
        for book in books:
            childrenText=self.getNodeOfChildText(book)
            dataList.append(childrenText)
        return dataList

if __name__ == "__main__":
     xml=ParseXML(r"C:\Users\ali\PycharmProjects\ExcelDataDrivenProject\TestDataXML.xml")
     datas=xml.getDataFromXML()
     for i in datas:
         print i["name"],i["author"]