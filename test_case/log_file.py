#! user/bin/python
'''
代码说明：测试输出报告
编写日期：
设置者：linux超
'''

import time

class login_log(object):
    def __init__(self,path='',mode='w'):
        filename = path + time.strftime('%Y-%m-%d',time.gmtime())
        self.log = open(path+filename+'.txt',mode)
    def log_write(self,msg):
        self.log.write(msg)
    def log_close(self):
        self.log.close()
if __name__ == '__main__':
    log=login_log()
    ftitle = time.strftime('%Y-%m-%d',time.gmtime())
    log.log_write('xiaochao11520')
    log.log_close()