#encoding=utf-8
#P213-214
import time
from datetime import datetime
'''
本文件用于获取当前日期以及时间
用于生成保存截图文件目录名
'''
def currentDate():
    date=time.localtime()
    today=str(date.tm_year)+'-'+str(date.tm_mon)+'-' + str(date.tm_mday)
    return today

def currentTime():
    timeStr=datetime.now()
    now=timeStr.strftime('%H-%M-%S')
    return now

if __name__ == "__main__":
    print currentDate()
    print currentTime()
