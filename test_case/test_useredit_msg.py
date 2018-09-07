#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-07 14:42:24
# @Author  : weymouth (261229090@qq.com)
# @Link    : http://blog.csdn.net/dkwyh547
# @Version : $Id$

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from modules.modules_test import HTS_login, HTS_loginout
from modules.adduser import *
import unittest
import time


class UserEdit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://39.105.53.51:8897"
        self.verificationErrors = []
        self.accept_next_alert = True

    def testuseredit_msg(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        adduser_dict = adduser(r'E:\auto case\python-selenium\modules\adduser.txt')
        HTS_login(driver, adduser_dict['un'], adduser_dict['pd'])
        # 打开用户管理页面
        findLinkText(driver, "用户管理").click()
        findCss(driver, ".in > li:nth-child(1) > a:nth-child(1)").click()
        time.sleep(3)
        # 查询新增数据
        driver.switch_to.frame("iframe1")
        findCss(driver, '#tree_table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(6) > a:nth-child(1)').click()
        findId(driver, 'name').send_keys('1')
        email = findCss(driver, '#email').get_attribute('value')
        email1 = list(email)
        nPos = email1.index('@')
        email1.insert(nPos, '3')
        email2 = "".join(email1)
        findId(driver, 'email').clear()
        findId(driver, 'email').send_keys(email2)
        findId(driver, 'phone').send_keys(Keys.BACKSPACE, '3')
        findId(driver, 'mobile').send_keys(Keys.BACKSPACE, '0')
        findCss(driver, 'button.btn:nth-child(1)').click()
        noticmsg = findCss(driver,
                           "body > div.wrapper > div.alert.alert-success.alert-block.fade.in > p").text
        msg1 = '保存用户信息成功！'
        if msg1 == noticmsg:
            print(noticmsg)
        else:
            print('保存用户信息失败！')
            driver.get_screenshot_as_file("E:/base_test/screenshot/useredit_msg_false.png")
            driver.switch_to.default_content()
            HTS_loginout(driver)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()