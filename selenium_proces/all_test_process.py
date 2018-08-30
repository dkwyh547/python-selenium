#coding=utf-8
import unittest, time, os, multiprocessing
import commands
from email.mime.text import MIMENonMultipart
import HTMLTestRunner
import sys, pickle

sys.path.append('E:\\auto case\\python-selenium\\selenium_proces')

def EEEcreatsuite1():
    casedir=[]
    listaa=os.listdir(r'E:\auto case\python-selenium\selenium_proces')
    for xx in listaa:
        if "thread" in xx:
            casedir.append(xx)
    print(casedir)
    suite=[]
    for n in casedir:
        testunit=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(str(n),pattern='test_*.py',top_level_dir='E:\\')
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTest(test_case)
                #print testunit
        suite.append(testunit)
    return suite,casedir
def EEEEEmultiRunCase(suite, casedir):
    global runner, i
    now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
    filename = 'E:\\auto case\python-selenium\\result\\ '+now+'result.html'
    fp = open(filename, 'wb')
    #pickle.dump(proclist, fp)
    #proclist = pickle.load(fp)
    proclist = []
    s=0
    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(
                                                stream=fp,
                                                title=str(casedir[s])+u'测试报告',
                                                description=u'用例执行情况：'
                                                )
    proc = multiprocessing.Process(target=runner.run,args=(i,))
    proclist.append(proc)
    s=s+1
    #fp.close()
    #fp = open(filename, 'rb')
    #proclist = pickle.load(fp)
    #print (proclist)
    #print (s)
    #print (proc)
    for proc in proclist: proc.start()
    for proc in proclist: proc.join()
    fp.close()
if __name__ == "__main__":
    runtmp=EEEcreatsuite1()
    EEEEEmultiRunCase(runtmp[0],runtmp[1])
