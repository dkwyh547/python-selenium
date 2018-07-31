#coding=utf-8
import unittest, time, os, multiprocessing
import commands
from email.mime.text import MIMEText
import HTMLTestRunner
import sys

sys.path.append('\selenium_proces')

def EEEcreatsuite1():
    casedir=[]
    listaa=os.listdir('C:\\Users\\neunn\\Documents\\wushixin\\eclipse_job\\workspaces\\PythonCase\\src\\Python27\\selenium_proces\\')
    for xx in listaa:
        if "thread" in xx:
            casedir.append(xx)
    print casedir
    suite=[]
    for n in casedir:
        testunit=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(str(n),pattern='test_*.py',top_level_dir='C:\\Users\\neunn\\Documents\\wushixin\\eclipse_job\\workspaces\\PythonCase\\src\\Python27\\')
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)
                #print testunit
            suite.append(testunit)
    return suite,casedir

def EEEEEmultiRunCase(suite,casedir):
    now = time.strftime('%Y-%m-%d-%H_%M_%S_',time.localtime(time.time()))
    filename = 'C:\\Users\\neunn\\Documents\\wushixin\\eclipse_job\\workspaces\\PythonCase\\src\\Python27\\result\\'+now+'result.html'
    fp = file(filename, 'wb')
    proclist=[]
    s=0
    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=str(casedir[s])+u'测试报告',description=u'用例执行情况：')
        proc = multiprocessing.Process(target=runner.run,args=(i,))
        proclist.append(proc)
        s=s+1
    for proc in proclist: proc.start()
    for proc in proclist: proc.join()
    fp.close()
if __name__ == "__main__":
    runtmp=EEEcreatsuite1()
    EEEEEmultiRunCase(runtmp[0],runtmp[1])
