if __name__ == "__main__":
    #定义一个单元测试容器
    testunit=unittest.TestSuite()
    #将测试用例加入到测试容器中
    testunit.addTest(Baidu("test_baidu_search"))
    testunit.addTest(Baidu("test_baidu_set"))
    #取当前时间
    now=time.strftime("%Y-%m-%M-%H_%M_%S_",time.localtime(time.time()))
    #定义个报告存放路径，支持相对路径
    filename = "D:\\selenium_python\\report\\result.html"+now+'result.html'
    fp = file(filename, 'wb')
    #定义测试报告
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'百度搜索测试报告',
        description=u'用例执行情况：')

    #运行测试用例
    runner.run(testunit)
