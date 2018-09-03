from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException
from modules.modules_test import *
from test_case.adduser import *
from package.location import *
import unittest


class UserControl(unittest.TestCase):
    def setUp(self):
        HTS_http(driver, ele_dict)
        self.verificationErrors = ()
        self.accept_next_alert = True
        HTS_login(driver, 'wushixin', 'wushixin')

    def add_user(self):
        # 打开用户管理页面
        findLinkText(driver,"用户管理").click()
        findCss(driver,".in > li:nth-child(1) > a:nth-child(1)").click()
        # 新增用户按钮
        driver.switch_to_frame("iframe1")
        findId(driver,"button_post_insert").click()
        # 输入新增用户名称
        findId(driver,"name").clear()
        findId(driver,"name").send_keys(adduser_dict['name'])
        # 输入新增用户用户名
        findId(driver,"login_name").clear()
        findId(driver,"login_name").send_keys(adduser_dict['login_name'])
        # 输入新增用户密码
        findId(driver,"password").clear()
        findId(driver,"password").send_keys(adduser_dict['pwd'])
        # 输入新增用户确认密码
        findId(driver,"confirmNewPassword").clear()
        findId(driver,"confirmNewPassword").send_keys(adduser_dict['confirmNewPassword'])
        # 输入email信息
        findId(driver,"email").clear()
        findId(driver,"email").send_keys(adduser_dict['email'])
        # 输入电话信息
        findId(driver,"phone").clear()
        findId(driver,"phone").send_keys(adduser_dict['phone'])
        # 输入手机号信息
        findId(driver,"mobile").clear()
        findId(driver,"mobile").send_keys(adduser_dict['mobile'])
        # 选择是否允许登录
        findCss(driver,"label.radio-inline:nth-child(1) > input:nth-child(1)").click()
        # 选择系统权限
        findClassName(driver,"chosen-choices").click()
        findClassName(driver,"active-result").click()
        # 选择全部权限
        findCss(driver,"label.checkbox-inline:nth-child(3) > input:nth-child(1)").click()
        # 点击保存按钮
        findXpath(driver,"/html/body/div[1]/section/header/span/button[1]").click()

    def check_user(self):
        # 退出当前用户
        driver.switch_to_default_content()
        HTS_logout(driver)
        # 登录新创建用户
        HTS_login(driver, adduser_dict['login_name'], adduser_dict['pwd'])
        # 打开用户管理页面
        findLinkText(driver,"用户管理").click()
        findCss(driver,".in > li:nth-child(1) > a:nth-child(1)").click()
        # 获取用户管理列表第一行数据
        listdata = findCss(driver,'#tree_table > tbody:nth-child(2) > tr:nth-child(1)')
        listdata = listdata.text
        listdata = listdata.split(' ')
        listsend = []
        listsend = adduser_dict.values()
        listsend.append('编辑')
        listsend.append('删除')
        listsend.append('密码重置')
        print(operator.eq(listsend, listdata))

    def is_element_present(self, how, what):
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException as e:return False
        return True

    def is_alert_present(self):
        try:
            driver.switch_to_alert()
        except NoAlertPresentException as e:return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


    def tearDown(self):
        HTS_logout(driver)
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
        unittest.main()
