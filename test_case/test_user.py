import unittest,time,os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from modules.modules_test import *

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://39.106.240.149/")
HTS_login(drver)
driver.find_element_by_css_selector(".dropdown-toggle").click()
driver.find_element_by_css_selector(".dropdown-alerts > li:nth-child(7) > a:nth-child(1)").click()
driver.find_element_by_link_text("用户管理").click()
driver.find_element_by_css_selector(".in > li:nth-child(1) > a:nth-child(1)").click()
driver.switch_to_frame("iframe1")
driver.find_element_by_id("button_post_insert").click()
