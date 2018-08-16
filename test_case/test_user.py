import unittest,time,os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from modules.modules_test import *

#访问系统首页
HTS_http('http://39.106.240.149/')
#登录系统
HTS_login(driver, 'wushixin', 'wushixin')
#打开用户管理页面
driver.find_element_by_link_text("用户管理").click()
driver.find_element_by_css_selector(".in > li:nth-child(1) > a:nth-child(1)").click()
#新增用户按钮
driver.switch_to_frame("iframe1")
driver.find_element_by_id("button_post_insert").click()
#输入新增用户名称
driver.find_element_by_id("name").clear()
driver.find_element_by_id("name").send_keys("test10")
#输入新增用户用户名
driver.find_element_by_id("login_name").clear()
driver.find_element_by_id("login_name").send_keys("testabc")
#输入新增用户密码
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
#输入新增用户确认密码
driver.find_element_by_id("confirmNewPassword").clear()
driver.find_element_by_id("confirmNewPassword").send_keys("123456")
#选择是否允许登录
driver.find_element_by_css_selector("label.radio-inline:nth-child(1) > input:nth-child(1)").click()
#选择系统权限
driver.find_element_by_class_name("chosen-choices").click()
driver.find_element_by_class_name("active-result").click()
#选择全部权限
driver.find_element_by_css_selector("label.checkbox-inline:nth-child(3) > input:nth-child(1)").click()
#点击保存按钮
driver.find_element_by_xpath("/html/body/div[1]/section/header/span/button[1]").click()
#退出当前用户
driver.switch_to_default_content()
HTS_logout(driver)
#登录新创建用户
HTS_login(driver, 'test10', '123456')
#打开用户管理页面
driver.find_element_by_link_text("用户管理").click()
driver.find_element_by_css_selector(".in > li:nth-child(1) > a:nth-child(1)").click()
#获取用户管理列表第一行数据
listdata = driver.find_element_by_css_selector('#tree_table > tbody:nth-child(2) > tr:nth-child(1)')
listdata = listdata.text
listdata = listdata.split(' ')
