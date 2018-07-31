#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com/")

driver.find_element_by_name("tj_settingicon").click()
driver.find_element_by_id("sh_2").click()

driver.find_element_by_id("save").click()

alert=driver.switch_to_alert()

alert.accept()

alert=driver.switch_to_alert()

print alert.text()

driver.quit()