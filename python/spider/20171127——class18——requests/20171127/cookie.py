#-*-coding:utf-8-*-
import requests

user_agent="Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"
referer="http://www.xicidaili.com/nn/1"
headers={"User_Agent":user_agent,"Referer":referer}
cookies={"ww":'123'}
response=requests.get("https://www.baidu.com/baidu?wd=%E5%87%A1%E7%A7%91%E5%BB%BA%E7%AB%99%E7%99%BB%E5%BD%95&tn=monline_4_dg&ie=utf-8",headers=headers,cookies=cookies)

for key in response.cookies.keys():
	print key+"------"+response.cookies.get(key)