#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time
#登陆模块（函数）

def login(self):
    driver = self.driver
    driver.get(self.base_url + "/")
    driver.find_element_by_id("username").send_keys('wushixin')
    driver.find_element_by_id("password").send_keys('wushixin')
    driver.find_element_by_id("login_btn").click()
    time.sleep(10)
    driver.switch_to.frame("iframe_system")
    t1 = driver.find_element_by_css_selector("div.alert:nth-child(1)")
    t1 = t1.text
    t2 = "欢迎 wushixin 登录管理中心"
    if t1 == t2:
        print("登录成功")
    else:
        print("登录失败")
        driver.get_screenshot_as_png("E:/base_test/screenshot/login_false.png")
    driver.switch_to_default_content()
