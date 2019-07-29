#-*-coding:utf-8-*-
#python2
#导入urllib库
from urllib2 import urlopen
from bs4 import BeautifulSoup
from urllib2 import HTTPError


def getImg(url):
	try:
		#打开一个连接返回一个响应对象(http.client.HTTPResponse)
		response=urlopen(url)
	except HTTPError as e:
		return None

	try:
		#调用响应对象打read()函数，获取该服务器响应的数据
		#print html
		html=response.read()
		#把html传给BeautifulSoup对象
		bsObj=BeautifulSoup(html)
		#通过bsObj获img标签
		i=bsObj.p.a
		print i
	except AttributeError as e:
		print "没有找到标签"



if __name__=="__main__":
	getImg("http://www.pythonscraping.com/pages/page1.html")
