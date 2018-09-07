#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-07 10:17:09
# @Author  : weymouth (261229090@qq.com)
# @Link    : http://blog.csdn.net/dkwyh547
# @Version : $Id$

from selenium import webdriver
from package.location import *
from modules.modules_test import HTS_loginout, HTS_login
from modules.adduser import *
import unittest
import time


class UserAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://39.105.53.51:8897"
        self.verificationErrors = []
        self.accept_next_alert = True

    def testuseradd(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        adduser_dict = adduser(r'E:\auto case\python-selenium\modules\adduser.txt')
        HTS_login(driver, adduser_dict['un'], adduser_dict['pd'])
        infomsg = findCss(driver, '#gritter-item-1 > div.gritter-item').text
        driver.switch_to.frame("iframe_system")
        t1 = findCss(driver, "div.alert:nth-child(1)").text
        t2 = "欢迎" + " " + adduser_dict['un'] + " " + "登录管理中心"
        if t1 == t2:
            print("登录成功")
            print(infomsg)
        else:
            print("登录失败")
            driver.get_screenshot_as_file(
                "E:/base_test/screenshot/login1_false.png")
        driver.switch_to.default_content()
        time.sleep(3)
        # 打开用户管理页面
        findLinkText(driver, "用户管理").click()
        findCss(driver, ".in > li:nth-child(1) > a:nth-child(1)").click()
        time.sleep(3)
        # 新增用户按钮
        driver.switch_to.frame("iframe1")
        findId(driver, "button_post_insert").click()
        time.sleep(3)
        # 输入新增用户名称
        findId(driver, "name").clear()
        findId(driver, "name").send_keys(adduser_dict['name'])
        # 输入新增用户用户名
        findId(driver, "login_name").clear()
        findId(driver, "login_name").send_keys(adduser_dict['login_name'])
        # 输入新增用户密码
        findId(driver, "password").clear()
        findId(driver, "password").send_keys(adduser_dict['pwd'])
        # 输入新增用户确认密码
        findId(driver, "confirmNewPassword").clear()
        findId(driver, "confirmNewPassword").send_keys(
            adduser_dict['confirmNewPassword'])
        # 输入email信息
        findId(driver, "email").clear()
        findId(driver, "email").send_keys(adduser_dict['email'])
        # 输入电话信息
        findId(driver, "phone").clear()
        findId(driver, "phone").send_keys(adduser_dict['phone'])
        # 输入手机号信息
        findId(driver, "mobile").clear()
        findId(driver, "mobile").send_keys(adduser_dict['mobile'])
        # 选择是否允许登录
        findCss(driver, "label.radio-inline:nth-child(1) > input:nth-child(1)").click()
        # 选择系统权限
        findClassName(driver, "chosen-choices").click()
        findClassName(driver, "active-result").click()
        # 选择全部权限
        findCss(
            driver, "label.checkbox-inline:nth-child(3) > input:nth-child(1)").click()
        # 点击保存按钮
        findXpath(
            driver, "/html/body/div[1]/section/header/span/button[1]").click()
        time.sleep(3)
        noticmsg = findCss(driver,
                           "body > div.wrapper > div.alert.alert-success.alert-block.fade.in > p").text
        print(noticmsg)
    # check用户
        # 退出当前用户
        driver.switch_to.default_content()
        HTS_loginout(driver)
        # 登录新创建用户
        HTS_login(driver, adduser_dict['login_name'], adduser_dict['pwd'])
        infomsg = findCss(driver, '#gritter-item-1 > div.gritter-item').text
        driver.switch_to.frame("iframe_system")
        t1 = driver.find_element_by_css_selector("div.alert:nth-child(1)").text
        t3 = "欢迎" + " " + adduser_dict['name'] + " " + "登录管理中心"
        if t1 == t3:
            print("登录成功")
            print(infomsg)
        else:
            print("登录失败")
            driver.get_screenshot_as_file(
                "E:/base_test/screenshot/login2_false.png")
        driver.switch_to.default_content()
        # 退出当前用户
        HTS_loginout(driver)
    # 驱动退出

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
