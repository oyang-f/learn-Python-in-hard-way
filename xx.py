#-*- coding: UTF-8 -*-
import urllib2
response=urllib2.urlopen('http://www.gxeduyun.edu.cn')
html=response.read()
print html
