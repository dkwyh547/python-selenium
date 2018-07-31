# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("#u1 > a[name=\"tj_login\"]").click()
        driver.find_element_by_id("TANGRAM__PSP_8__userName").clear()
        driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("13082400605")
        driver.find_element_by_id("TANGRAM__PSP_8__password").clear()
        driver.find_element_by_id("TANGRAM__PSP_8__password").send_keys("dk5013226")
        driver.find_element_by_id("TANGRAM__PSP_8__memberPass").click()
        driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
        driver.find_element_by_css_selector("span.user-name").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("//div[@id='ibx-mod-history-box']/div/div/div/span").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-history']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-video']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-nuomi']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-xinwen']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-lvyou']/div/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-koubei']/div/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-picture']/div/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-music']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-tieba']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-chuanke']/div/ul/li[3]").click()
        driver.find_element_by_xpath("//div[@id='ibx-picture']/div/span").click()
        driver.find_element_by_xpath("//div[@id='ibx-lvyou']/div/div/span").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-zhidao']/div/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='ibx-chuanke']/div/div/span").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-tieba']/div/ul/li[3]").click()
        driver.find_element_by_link_text(u"明天").click()
        driver.find_element_by_link_text(u"后天").click()
        driver.find_element_by_link_text("08.11").click()
        driver.find_element_by_link_text("08.12").click()
        driver.find_element_by_css_selector("a.ibx-cal-tocal").click()
        driver.find_element_by_link_text(u"13 十一").click()
        driver.find_element_by_id("add-cal-popup").clear()
        driver.find_element_by_id("add-cal-popup").send_keys("test")
        driver.find_element_by_css_selector("span.ecl-ui-tip-body-save").click()
        driver.find_element_by_link_text(u"返回").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-history-box']/div/div/div/span").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-history']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-video']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-nuomi']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-picture']/div/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-lvyou']/div/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-xinwen']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-koubei']/div/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-tieba']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-music']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='ibx-mod-zhidao']/div/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='ibx-lvyou']/div/div/span").click()
        driver.find_element_by_xpath("//div[@id='ibx-chuanke']/div/div/span").click()
        driver.find_element_by_css_selector("a.ibx-uc-nick").click()
        driver.find_element_by_id("passport-sex-1").click()
        driver.find_element_by_css_selector("div.cus-sel-opt-panel").click()
        driver.find_element_by_link_text("1988").click()
        driver.find_element_by_css_selector("#cussel1000001 > div.cus-sel-opt-panel").click()
        driver.find_element_by_link_text("10").click()
        driver.find_element_by_css_selector("#cussel1000002 > div.cus-sel-opt-panel").click()
        driver.find_element_by_link_text(u"其他").click()
        driver.find_element_by_css_selector("#cussel1000003 > div.cus-sel-opt-panel").click()
        driver.find_element_by_link_text(u"辽宁").click()
        driver.find_element_by_css_selector("#cussel1000008 > div.cus-sel-opt-panel").click()
        driver.find_element_by_link_text(u"沈阳").click()
        driver.find_element_by_css_selector("#cussel1000009 > div.cus-sel-opt-panel").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'其他')])[4]").click()
        driver.find_element_by_css_selector("#cussel1000005 > div.cus-sel-opt-panel").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'辽宁')])[2]").click()
        driver.find_element_by_css_selector("#cussel1000010 > div.cus-sel-opt-panel").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'沈阳')])[2]").click()
        driver.find_element_by_css_selector("#cussel1000011 > div.cus-sel-opt-panel").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'其他')])[7]").click()
        driver.find_element_by_id("passport_userdetail").clear()
        driver.find_element_by_id("passport_userdetail").send_keys(u"补充资料")
        driver.find_element_by_css_selector("#cussel1000007 > div.cus-sel-opt-panel").click()
        driver.find_element_by_xpath("(//a[contains(text(),'8')])[22]").click()
        driver.find_element_by_css_selector("input.setting-submit-btn.setting-submit-ml100").click()
        driver.find_element_by_link_text(u"详细资料").click()
        driver.find_element_by_css_selector("div.cus-sel-opt-panel").click()
        driver.find_element_by_link_text(u"运动型").click()
        driver.find_element_by_css_selector("#cussel1000001 > div.cus-sel-opt-panel").click()
        driver.find_element_by_link_text(u"单身").click()
        driver.find_element_by_id("passport-character-10").click()
        driver.find_element_by_id("passport-character-3").click()
        driver.find_element_by_id("passport-character-6").click()
        driver.find_element_by_id("cussel1000005").click()
        driver.find_element_by_link_text(u"大学").click()
        driver.find_element_by_id("cussel1000006").click()
        driver.find_element_by_id("stthld").click()
        driver.find_element_by_css_selector("#cussel1000006 > div.cus-sel-opt-panel").click()
        driver.find_element_by_link_text(u"计算机/电子产品").click()
        driver.find_element_by_css_selector("input.setting-submit-btn.setting-submit-ml100").click()
    
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
