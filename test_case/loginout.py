#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time
#登出模块（函数）

def loginout(self):
    driver = self.driver
    driver.find_element_by_css_selector(".dropdown-toggle").click()
    driver.find_element_by_css_selector(".dropdown-alerts > li:nth-child(7) > a:nth-child(1)").click()
