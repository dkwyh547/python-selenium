#coding=utf-8
import unittest
#把test_case目录添加到path，这里用的相对路径
import sys
sys.path.append("\test_case")
#这里需要导入测试文件
from test_case import baidu
from test_case import youdao
import baidu,youdao
import HTMLTestRunner

testunit=unittest.TestSuite()
#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))
#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)
#定义个报告存放路径，支持相对路径。
filename = 'D:\\selenium_python\\report\\result2.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况：')

#执行测试用例
runner.run(testunit)