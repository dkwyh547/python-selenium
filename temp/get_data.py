import urllib.request
import http.cookiejar

url = 'http://www.baidu.com/'

print('方法二')
res_two = urllib.request.urlopen(url)
code_two = res_two.getcode()
html_two = res_two.read().decode('utf-8')
print('方法二网页状态码：%s' % (code_two))
print('方法二网页内容：'+html_two)