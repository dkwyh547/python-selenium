#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-07 13:38:06
# @Author  : weymouth (261229090@qq.com)
# @Link    : http://blog.csdn.net/dkwyh547
# @Version : $Id$

from selenium import webdriver
from modules.modules_test import HTS_login, HTS_loginout
from test_case.adduser import *
import unittest
import time


class UserQuery(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://39.105.53.51:8897"
        self.verificationErrors = []
        self.accept_next_alert = True

    def testuserquery(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        adduser_dict = adduser(r'E:\auto case\python-selenium\modules\adduser.txt')
        HTS_login(driver, adduser_dict['login_name'], adduser_dict['pwd'])
        # 打开用户管理页面
        findLinkText(driver, "用户管理").click()
        findCss(driver, ".in > li:nth-child(1) > a:nth-child(1)").click()
        time.sleep(3)
        # 查询新增数据
        driver.switch_to.frame("iframe1")
        findId(driver, 'name').send_keys(adduser_dict['name'])
        findCss(driver,
                'section.panel:nth-child(4) > header:nth-child(1) > span:nth-child(1) > button:nth-child(1)').click()
        time.sleep(2)
        # 获取用户管理列表第一行数据
        listdata = findCss(
            driver, '#tree_table > tbody:nth-child(2) > tr:nth-child(1)').text
        listdata = listdata.split(' ')
        listdata = listdata[0:5]
        listsend = list(adduser_dict.values())
        listsend = listsend[0:5]
        result = operator.eq(listsend, listdata)
        if result is True:
            print('userquery is True')
        else:
            print('userquery is false')
            driver.get_screenshot_as_file(
                "E:/base_test/screenshot/adduser_false.png")
        # 退出当前用户
        HTS_loginout(driver)
        driver.switch_to.default_content()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
