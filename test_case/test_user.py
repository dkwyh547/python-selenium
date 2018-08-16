import unittest,time,os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from modules.modules_test import *

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://39.106.240.149/")
un='wushixin'
pw='wushixin'
HTS_login(driver)
driver.find_element_by_link_text("用户管理").click()
driver.find_element_by_css_selector(".in > li:nth-child(1) > a:nth-child(1)").click()
driver.switch_to_frame("iframe1")
driver.find_element_by_id("button_post_insert").click()
driver.find_element_by_id("name").clear()
driver.find_element_by_id("name").send_keys("test01")
driver.find_element_by_id("login_name").clear()
driver.find_element_by_id("login_name").send_keys("testwsx")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("confirmNewPassword").clear()
driver.find_element_by_id("confirmNewPassword").send_keys("123456")
driver.find_element_by_css_selector("label.radio-inline:nth-child(1) > input:nth-child(1)").click()
driver.find_element_by_class_name("chosen-choices").click()
driver.find_element_by_class_name("active-result").click()
#选择全部权限
driver.find_element_by_css_selector("label.checkbox-inline:nth-child(3) > input:nth-child(1)").click()
driver.find_element_by_xpath("/html/body/div[1]/section/header/span/button[1]").click()
driver.find_element_by_css_selector(".dropdown-toggle").click()
driver.find_element_by_css_selector(".dropdown-alerts > li:nth-child(7) > a:nth-child(1)").click()
un = 'testwsx'
pw = '123456'
HTS_login(driver)
