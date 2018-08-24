from selenium import webdriver
import unittest
import pymysql
import codecs

def webinfo(path):
    file = codecs.open(path,'r','gbk')
    ele_dict = {}
    for line in file:
        result = [ele.strip() for ele in line.split('=')]
        ele_dict.update(dict([result]))
    return ele_dict



#定义访问函数
def HTS_http(ele_dict):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get(ele_dict['Turl'])

#定义mysql连接函数
def HTS_consql(dbname):
    # 打开数据库连接
    db = pymysql.connect(host="39.106.121.185", user="root",
                         password="!QAZ@WSx", db=dbname, port=3306)

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

#定义登录函数
def HTS_login(driver, username, password):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
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

#定义退出函数
def HTS_logout(driver):
    driver.find_element_by_css_selector(".dropdown-toggle").click()
    driver.find_element_by_css_selector(".dropdown-alerts > li:nth-child(7) > a:nth-child(1)").click()
    driver.quit()

if __name__ == "__main__":
    unittest.main()
    ele_dict = webinfo(r'E:\auto case\python-selenium\modules\webinfo.txt')
    for key in ele_dict:
        print(key,ele_dict[key])