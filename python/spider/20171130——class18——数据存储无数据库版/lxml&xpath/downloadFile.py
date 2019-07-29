#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
from urllib import urlretrieve
import uuid

#回调函数
def fun1(blocknum,blocksize,totalsize):
    '''
    :param blocknum: 下载的数据块的个数
    :param blocksize: 下载的数据块的大小
    :param totalsize: 文件的总大小
    :return:
    '''
    #计算下载的数据的百分比
    per=100.0*blocknum*blocksize/totalsize
    if per>100:
        per=100
        print "当前下载百分之%s"%per





user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:44.0) Gecko/20100101 Firefox/44.0"
headers = {"User_Agent": user_agent}
response=requests.get("http://www.ivsky.com/tupian/ziranfengguang/",headers=headers)
html=response.text

soup=BeautifulSoup(html,"lxml")
imgs=soup.find_all("img")
for img in imgs:
    src=img.attrs.get("src")
    #下载数据
    filename,headers=urlretrieve(src,"images/"+str(uuid.uuid1())+src[src.rfind("."):],fun1)
    print filename
    print headers