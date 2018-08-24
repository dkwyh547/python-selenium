import unittest,time,os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from modules.modules_test import *
from package.location import *
import operator

#访问系统首页
HTS_http('http://39.106.240.149/')
#登录系统
HTS_login(driver, 'wushixin', 'wushixin')
#打开用户管理页面
findLinkText("用户管理").click()
findCss(".in > li:nth-child(1) > a:nth-child(1)").click()
#新增用户按钮
driver.switch_to_frame("iframe1")
findId("button_post_insert").click()
#输入新增用户名称
findId("name").clear()
findId("name").send_keys("test10")
#输入新增用户用户名
findId("login_name").clear()
findId("login_name").send_keys("testabc")
#输入新增用户密码
findId("password").clear()
findId("password").send_keys("123456")
#输入新增用户确认密码
findId("confirmNewPassword").clear()
findId("confirmNewPassword").send_keys("123456")
#输入email信息
findId("email").clear()
findId("email").send_keys("261229090@qq.com")
#输入电话信息
findId("phone").clear()
findId("phone").send_keys("0241-5013226")
#输入手机号信息
findId("mobile").clear()
findId("mobile").send_keys("18204017653")
#选择是否允许登录
findCss("label.radio-inline:nth-child(1) > input:nth-child(1)").click()
#选择系统权限
findClassName("chosen-choices").click()
findClassName("active-result").click()
#选择全部权限
findCss("label.checkbox-inline:nth-child(3) > input:nth-child(1)").click()
#点击保存按钮
findXpath("/html/body/div[1]/section/header/span/button[1]").click()
#退出当前用户
driver.switch_to_default_content()
HTS_logout(driver)
#登录新创建用户
HTS_login(driver, 'test10', '123456')
#打开用户管理页面
findLinkText("用户管理").click()
findCss(".in > li:nth-child(1) > a:nth-child(1)").click()
#获取用户管理列表第一行数据
listdata = findCss('#tree_table > tbody:nth-child(2) > tr:nth-child(1)')
listdata = listdata.text
listdata = listdata.split(' ')
listsend = ['test10', 'testabc', '0241-5013226', '18204017653', '261229090@qq.com' , '编辑', '删除', '密码重置']
print(operator.eq(listsend,listdata))