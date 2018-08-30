from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://39.105.53.51:8897"
        self.verificationErrors = []
        self.accept_next_alert = True
    #登录用例
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("username").send_keys('wushixin')
        driver.find_element_by_id("password").send_keys('wushixin')
        driver.find_element_by_id("login_btn").click()
        time.sleep(10)
        driver.switch_to.frame("iframe_system")
        t1 = driver.find_element_by_css_selector("div.alert:nth-child(1)").text
        t2 = "欢迎 wushixin 登录管理中心"
        if t1 == t2:
            print("login_ok")
        else:
            print("login_false_")
            driver.get_screenshot_as_png("E:\\auto case\\python-selenium\\screenshot\\login_false.png")
        driver.switch_to_default_content()
    #用户退出
    def test_loginout(self):
        driver = self.driver
        driver.find_element_by_css_selector(".dropdown-toggle").click()
        driver.find_element_by_css_selector(".dropdown-alerts > li:nth-child(7) > a:nth-child(1)").click()
    #驱动退出
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
