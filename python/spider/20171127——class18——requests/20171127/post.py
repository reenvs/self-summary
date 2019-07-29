#-*-coding:utf-8-*-
import requests
import chardet

#data={"username":"zhangsan","password":"123456"}
#r=requests.post("http://127.0.0.1:8000/login",data=data)
#print type(r) 
r=requests.get("https://wwww.baidu.com")
r.encoding=chardet.detect(r.content).get('encoding')
print r.encoding
print r.text
