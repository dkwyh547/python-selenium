#coding=utf-8
#把 test_case 目录添加到 path 下，这里用的相对路径
import sys
sys.path.append(r"\test_case")
from test_case import *
#用例文件列表
def caselist():
    alltestnames = [baidu.Baidu,youdao.Youdao,webcloud.Login,]
print "success read case list!!"
return alltestnames
