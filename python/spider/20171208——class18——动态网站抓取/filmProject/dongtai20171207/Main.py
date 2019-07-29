#coding:utf-8
from HTMLDownloader import HtmlDownloader
from HtmlParser import HtmlParser
import time
import json

class Main(object):
    def __init__(self):
        self.download=HtmlDownloader()
        self.par=HtmlParser()



    def action(self,root_url):
        html=self.download.download(root_url)
        #通过解析器解析当前页面的url
        urls=self.par.parser_url(html)
        #遍历url并拼接url
        for url in urls:
            t=time.strftime("%Y%m%d%H%M%S2877",time.localtime())
            new_url="http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=%s&t=%s&Ajax_CallBackArgument0=%s"%(url[0],t,url[1])
            print new_url
            #新的url交给下载器下载
            detail_html=self.download.download(new_url)
            print detail_html
            self.par.parser_json(detail_html)

if __name__=="__main__":
    m=Main()
    m.action("http://theater.mtime.com/China_Beijing/")

