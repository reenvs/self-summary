#-*-coding:utf-8-*-
import requests

#使用get方式
#r=requests.get("http://127.0.0.1:8000/listDocByPager?sex=男")

data={'sex':'女'}
r=requests.get("http://127.0.0.1:8000/listDocByPager",params=data)
print r.content.decode("utf-8")