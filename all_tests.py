#coding=utf-8
import unittest
#把test_case目录添加到path，这里用的相对路径
import sys
sys.path.append("E:\\auto case\\python-selenium\\test_case")
#这里需要导入测试文件
import test_login
import HTMLTestRunner

testunit = unittest.TestSuite()
#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(test_login.test_login)
#执行测试套件
runner = unittest.TextTestRunner()
runner.run(testunit)
#定义个报告存放路径，支持相对路径。
filename = 'E:\\auto case\\python-selenium\\result\\result2.html'
fp = open(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'测试报告',
    description=u'用例执行情况：')
