from modules.modules_test import *
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://39.106.240.149/")
HTS_login(driver,'wushixin','wushixin')