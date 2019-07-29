#coding:utf-8
#爬虫调度者
from HtmlDownloader import htmlDownloader
from HtmlParser import htmlParser
from HtmlSave import htmlSave
from UrlManager import UrlManager

class manage(object):

    def __init__(self):
        #创建一个url管理器
        self.urlManager=UrlManager()
        #创建一个html下载器
        self.downloader = htmlDownloader()
        #创建一个html的解析器
        self.htmlparser=htmlParser()
        #创建一个html的存储器
        self.htmlSave=htmlSave()

    def action(self):
        #给url管理器设置一个根url地址
        root_url="https://baike.baidu.com/item/网络爬虫"
        self.urlManager.add_new_url(root_url)
        n=0
        #询问url管理器是否有待取的url
        while self.urlManager.has_new_url() and n<=100:
            n+=1
            #获取一个未被抓取的url地址
            new_url=self.urlManager.get_new_url()
            #把url交给下载器去下载html代码
            htmlStr=self.downloader.download(new_url)
            #把htmlStr字符串交给解析器去解析，解析器返回一个元祖
            #元祖的第一值是和当前页面关联的所有的url，是一个set集合
            #元祖的第二个值是当前页面的数据，是一个字典
            urls,data=self.htmlparser.parser(new_url,htmlStr)
            #把urls交给url管理器
            self.urlManager.add_new_urls(urls)
            #把数据交给数据存储器
            self.htmlSave.saveData(data)
            print "第%s个页面的数据"%n
        self.htmlSave.output()


if __name__=="__main__":
    #创建一个调度器对象
    m=manage()
    m.action()



