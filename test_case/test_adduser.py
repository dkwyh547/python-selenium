from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from package.location import *
from adduser import *
#from adduser import adduser_dict
from modules.modules_test import *
import login, loginout
from pathlib import Path
import unittest, time, operator

class AddUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://39.105.53.51:8897"
        self.verificationErrors = []
        self.accept_next_alert = True
    def testadduser(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        login.login(self)
        time.sleep(3)
        adduser_dict = adduser(r'E:\auto case\python-selenium\test_case\adduser.txt')
        # 打开用户管理页面
        findLinkText(driver, "用户管理").click()
        findCss(driver, ".in > li:nth-child(1) > a:nth-child(1)").click()
        time.sleep(5)
        # 新增用户按钮
        driver.switch_to_frame("iframe1")
        findId(driver, "button_post_insert").click()
        time.sleep(5)
        # 输入新增用户名称
        findId(driver, "name").clear()
        findId(driver, "name").send_keys(adduser_dict['name'])
        # 输入新增用户用户名
        findId(driver, "login_name").clear()
        findId(driver, "login_name").send_keys(adduser_dict['login_name'])
        # 输入新增用户密码
        findId(driver, "password").clear()
        findId(driver, "password").send_keys(adduser_dict['pwd'])
        # 输入新增用户确认密码
        findId(driver, "confirmNewPassword").clear()
        findId(driver, "confirmNewPassword").send_keys(adduser_dict['confirmNewPassword'])
        # 输入email信息
        findId(driver, "email").clear()
        findId(driver, "email").send_keys(adduser_dict['email'])
        # 输入电话信息
        findId(driver, "phone").clear()
        findId(driver, "phone").send_keys(adduser_dict['phone'])
        # 输入手机号信息
        findId(driver, "mobile").clear()
        findId(driver, "mobile").send_keys(adduser_dict['mobile'])
        # 选择是否允许登录
        findCss(driver, "label.radio-inline:nth-child(1) > input:nth-child(1)").click()
        # 选择系统权限
        findClassName(driver, "chosen-choices").click()
        findClassName(driver, "active-result").click()
        # 选择全部权限
        findCss(driver, "label.checkbox-inline:nth-child(3) > input:nth-child(1)").click()
        # 点击保存按钮
        findXpath(driver, "/html/body/div[1]/section/header/span/button[1]").click()
        time.sleep(3)
    #check用户
        # 退出当前用户
        driver.switch_to_default_content()
        driver.find_element_by_css_selector(".dropdown-toggle").click()
        driver.find_element_by_css_selector(".dropdown-alerts > li:nth-child(7) > a:nth-child(1)").click()
        # 登录新创建用户
        HTS_login(driver, adduser_dict['  login_name'], adduser_dict['pwd'])
        # 打开用户管理页面
        findLinkText(driver, "用户管理").click()
        findCss(driver, ".in > li:nth-child(1) > a:nth-child(1)").click()
        # 获取用户管理列表第一行数据
        listdata = findCss(driver, '#tree_table > tbody:nth-child(2) > tr:nth-child(1)')
        listdata = listdata.text
        listdata = listdata.split(' ')
        listsend = adduser_dict.values()
        listsend.append('编辑')
        listsend.append('删除')
        listsend.append('密码重置')
        result = operator.eq(listsend, listdata)
        if result == True:
            print('adduser is True')
        else:
            print('adduser is false')
        driver.get_screenshot_as_file("E:/base_test/screenshot/adduser_false.png")
    #驱动退出
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
        unittest.main()
