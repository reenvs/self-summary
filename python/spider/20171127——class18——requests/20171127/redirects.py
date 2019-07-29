import requests

user_agent="Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"
referer="http://www.xicidaili.com/nn/1"
headers={"User_Agent":user_agent,"Referer":referer}
p={"http":"http://120.25.164.134:8118","http":"http://221.233.85.141:3128"}

r=requests.get("http://github.com",headers=headers,allow_redirects=True,proxies=p)
print r.url
print r.content