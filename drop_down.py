#-*-coding=utf-8
from selenium import webdriver
import os,time
driver= webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('drop_down.html')
driver.get(file_path)
time.sleep(2)

m=driver.find_element_by_id("ShippingMethod")
m.find_element_by_xpath("""//*[@id="ShippingMethod"]/option[3]""").click()
#m.find_element_by_xpath("//option[@value='10.69']").click()
time.sleep(3)
driver.quit()