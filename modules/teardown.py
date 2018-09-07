#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time
    #驱动退出
def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)
