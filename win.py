# coding: utf-8
from pywinauto.application import Application
import sys

if sys.getdefaultencoding() != 'gbk':
    reload(sys)
    sys.setdefaultencoding('gbk')
app = Application(backend="uia").start('notepad.exe')
# 查到这个记事本的控件树
dlg_spec = app['无标题 - 记事本']
dlg_spec.print_control_identifiers()