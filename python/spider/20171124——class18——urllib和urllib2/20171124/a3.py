#-*-coding:utf-8-*-
import urllib2
import urllib
import cookielib

#创建一个CookieJar对Cookie进行管理
c=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(c))
opener.addheaders.append(("Cookie","emai=sssssss"))
response=opener.open("http://localhost:8080/listPersonnelByPager")
for i in c:
	print i.name+" "+i.value