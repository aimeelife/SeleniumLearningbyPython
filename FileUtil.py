#encoding=utf-8
from DateUtil import currentTime,currentDate
import os

'''
P213-214
本文件主要用于创建目录，用于存放异常截图
方法仅供参考，具体应用时根据测试创建测试人员需要的目录或文件等
'''
def createDir():
    currentPath=os.path.dirname(os.path.abspath(__file__))
    today=currentDate()
    dateDir=os.path.join(currentPath,today)
    print dateDir
    if not os.path.exists(dateDir):
        os.mkdir(dateDir)
    now=currentTime()
    timeDir=os.path.join(dateDir,now)
    print timeDir
    if not os.path.exists(timeDir):
        os.mkdir(timeDir)
    return  timeDir

