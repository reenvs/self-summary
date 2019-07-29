#-*-coding:utf-8-*-
import requests

user_agent="Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"
referer="http://www.xicidaili.com/nn/1"
headers={"User_Agent":user_agent,"Referer":referer}

r=requests.get("http://www.xicidaili.com/nn/1",headers=headers)
print r.content.decode("utf-8")