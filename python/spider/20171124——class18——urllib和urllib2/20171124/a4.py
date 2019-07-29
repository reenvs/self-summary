#-*-coding:utf-8-*-
import urllib2
import urllib
import cookielib

try:
	response=urllib2.urlopen("http://localhost:8080/listPersonnelByPage")
	code=response.getcode()
	print code
except urllib2.HTTPError as e:
	print e.code
#html=response.read()
#print html