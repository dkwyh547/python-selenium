# -*- coding: utf-8 -*-
'''
Created on 2016��8��8��
@author: neunn
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BaiduDaohanglan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_baidu_daohanglan(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"糯米").click()
        driver.find_element_by_link_text(u"新闻").click()
        driver.find_element_by_link_text("hao123").click()
        driver.find_element_by_link_text(u"地图").click()
        driver.find_element_by_link_text(u"视频").click()
        driver.find_element_by_link_text(u"贴吧").click()
        driver.find_element_by_link_text(u"设置").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[6]/div/div/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[6]/span").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
