#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time

def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)
    time.sleep(3)
