#coding:utf-8
#导入模拟组合按键需要的包，以下5条
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import win32api
import win32clipboard as w
import win32con


#导入堆栈类
import traceback

#导入BY类
from selenium.webdriver.common.by import By
#导入显式等待类
from selenium.webdriver.support.ui import WebDriverWait
#导入期望场景类
from selenium.webdriver.support import expected_conditions as EC
#导入异常类
from selenium.common.exceptions import TimeoutException,NoSuchElementException

print "光荣之路"