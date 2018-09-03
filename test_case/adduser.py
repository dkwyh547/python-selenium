#! user/bin/python
'''
代码说明：从文本文档中读取用户管理数据
'''

import codecs

def adduser(path):
    file = codecs.open(path,'r','gbk')
    adduser_dict = {}
    for line in file:
        result = [adduser.strip() for adduser in line.split('=')]
        adduser_dict.update(dict([result]))
    return adduser_dict

if __name__ == '__main__':
    adduser_dict = adduser(r'E:\auto case\python-selenium\test_case\adduser.txt')
    for key in adduser_dict:
        print(key,adduser_dict[key])
