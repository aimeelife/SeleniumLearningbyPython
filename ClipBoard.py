#coding:utf-8
#p146
import win32clipboard as w
import win32con

#设置剪切板内容（写入）
def settext(aString):
   w.OpenClipboard()
   w.EmptyClipboard()
   w.SetClipboardData(win32con.CF_TEXT, aString)
   w.CloseClipboard()
   
#获取剪切板内容（读出）
def gettext():
   w.OpenClipboard()
   t = w.GetClipboardData(win32con.CF_TEXT)
   w.CloseClipboard()
   return t


paste = "Hello World！"

settext(paste)
print gettext()
