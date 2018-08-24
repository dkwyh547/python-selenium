#-*-coding=utf-8-*-
import os,unittest

caselist=os.listdir("E:\\auto case\\python-selenium\\test_case\\")
for a in caselist:
    s = a.split('.')[1]
    if s == 'py':
        os.system('E:\\auto case\\python-selenium\\test_case\\%s 1>>log.txt 2>&1' %a)

