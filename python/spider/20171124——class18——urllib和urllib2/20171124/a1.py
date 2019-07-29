#-*-coding:utf-8-*-
import urllib2
import urllib

#请求的url---------->http://127.0.0.1:8000/login
url="http://127.0.0.1:8000/login"
#传递的数据
postData={"username":"张三","password":"123456"}
print type(postData)
data=urllib.urlencode(postData)
print type(data)

#创建一个请求对象
request=urllib2.Request(url,data)
#响应
response=urllib2.urlopen(request)
html=response.read()
print html.decode("utf-8")