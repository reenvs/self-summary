#-*-coding:utf-8-*-
import requests

user_agent="Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"
referer="http://www.xicidaili.com/nn/1"
headers={"User_Agent":user_agent,"Referer":referer}

response=requests.get("https://wwww.baidu.com",headers=headers)
if response.status_code==200:
	print ("状态码："+str(response.status_code)).decode("utf-8")
	print response.headers
	print response.headers.get("Content-Type")#找不到返回None
	print response.headers["Content-Type"]#不建议使用，因为找不到会抛出一个异常
#print r.content.decode("utf-8")