# -*- coding: utf-8 -*-
import unittest, time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class BaiduDenglu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("#u1 > a.lb").click()
        time.sleep(3)
        driver.find_element_by_id("TANGRAM__PSP_8__userName").clear()
        driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("13082400605")
        driver.find_element_by_id("TANGRAM__PSP_8__password").clear()
        driver.find_element_by_id("TANGRAM__PSP_8__password").send_keys("dk5013226")
        driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
        time.sleep(10)
        above=driver.find_element_by_xpath("""//*[@id="s_username_top"]/span""")
        ActionChains(driver).move_to_element(above).perform()
        #left=driver.find_element_by_xpath("""//*[@id="s_username_top"]/span""")
        #ActionChains(driver).click_and_hold(left).perform()
        #element=driver.find_element_by_xpath("""//*[@id="s_username_top"]/span""")
        #target=driver.find_element_by_xpath("""//*[@id="s_user_name_menu"]/div/a[2]""")
        #ActionChains(driver).drag_and_drop(element,target).perform()
        #driver.find_element_by_xpath("""//*[@id="s_user_name_menu"]/div/a[2]""").click()
        driver.find_element_by_link_text(u"个人中心").click()
        #driver.find_element_by_xpath("//*[@id='s_user_name_menu']/div/a[2]").click()
        time.sleep(3)


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:return False
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
