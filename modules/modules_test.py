import unittest, time,os

from selenium import webdriver


def HTS_login(driver,username,password):
    driver.find_element_by_id("username").send_keys("username")
    driver.find_element_by_id("password").send_keys("password")
    driver.find_element_by_id("login_btn").click()
    driver.switch_to.frame("iframe_system")
    t1 = driver.find_element_by_css_selector("div.alert:nth-child(1)")
    t1 = t1.text
    t2 = "欢迎 wushixin 登录管理中心"
    if t1 == t2:
        print("pass")
    else:
        print("false")
    driver.switch_to_default_content()

def HTS_logout(driver):
    driver.find_element_by_css_selector(".dropdown-toggle").click()
    driver.find_element_by_css_selector(".dropdown-alerts > li:nth-child(7) > a:nth-child(1)").click()
    driver.quit()

if __name__ == "__main__":
    unittest.main()
