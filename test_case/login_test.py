#! user/bin/python
'''
代码说明：麦子学院登录模块自动化测试用例脚本
编写日期：
设置者：linux超
'''

import time
from selenium import webdriver
from webinfo import webinfo
from userinfo import userinfo
from log_fiile import login_log
from pathlib import Path

def open_web():
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver

def load_url(driver,ele_dict):
    driver.get(ele_dict['Turl'])
    time.sleep(5)

def find_element(driver,ele_dict):
    # find element
    driver.find_element_by_class_name(ele_dict['image_id']).click()
    if 'text_id' in ele_dict:
        driver.find_element_by_link_text('登录').click()

    user_id = driver.find_element_by_id(ele_dict['userid'])
    pwd_id = driver.find_element_by_id(ele_dict['pwdid'])
    login_id = driver.find_element_by_id(ele_dict['loginid'])
    return user_id,pwd_id,login_id

def send_val(ele_tuple,arg):
    # input userinfo
    listkey = ['uname','pwd']
    i = 0
    for key in listkey:
        ele_tuple[i].send_keys('')
        ele_tuple[i].clear()
        ele_tuple[i].send_keys(arg[key])
        i+=1
    ele_tuple[2].click()
def check_login(driver,ele_dict,log,userlist):
    result = False
    time.sleep(3)
    try:
        err = driver.find_element_by_id(ele_dict['error'])
        driver.save_screenshot(err.text+'.png')
        log.log_write('账号:%s 密码:%s 提示信息:%s:failed\n' %(userlist['uname'],userlist['pwd'],err.text))
        print('username or password error')
    except:
        print('login success!')
        log.log_write('账号:%s 密码:%s :passed\n'%(userlist['uname'],userlist['pwd']))
        #login_out(driver,ele_dict)
        return True
    return result
def login_out(driver,ele_dict):
    driver.find_element_by_class_name(ele_dict['logout']).click()
'''
def screen_shot(err):
    i = 0
    save_path = r'D:\pythondcode\capture'
    capturename = '\\'+str(i)+'.png'
    wholepath = save_path+capturename
    if Path(save_path).is_dir():
        pass
    else:
        Path(save_path).mkdir()
    while Path(save_path).exists():
        i+=1
        capturename = '\\'+str(i)+'.png'
        wholepath = save_path + capturename
    err.screenshot(wholepath)
'''
def login_test():
    log = login_log()
    #ele_dict = {'url': 'http://www.maiziedu.com/', 'text_id': '登录', 'user_id': 'id_account_l', 'pwd_id': 'id_password_l'
        #, 'login_id': 'login_btn','image_id':'close-windows-btn7','error_id':'login-form-tips'}
    ele_dict = webinfo(r'D:\pythoncode\webinfo.txt')
    #user_list=[{'uname':account,'pwd':pwd}]
    user_list = userinfo(r'D:\pythoncode\userinfo.txt')
    driver = open_web()
    # load url
    load_url(driver,ele_dict)
    #find element
    ele_tuple = find_element(driver,ele_dict)
    # send values
    ftitle = time.strftime('%Y-%m-%d', time.gmtime())
    log.log_write('\t\t\t%s登录系统测试报告\n' % (ftitle))
    for userlist in user_list:
        send_val(ele_tuple,userlist)
        # check login success or failed
        result = check_login(driver,ele_dict,log,userlist)
        if result:
            login_out(driver,ele_dict)
            time.sleep(3)
            ele_tuple = find_element(driver,ele_dict)
    time.sleep(3)
    log.log_close()
    driver.quit()

if __name__ == '__main__':
    login_test()