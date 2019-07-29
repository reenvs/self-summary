#coding:utf-8
from bs4 import BeautifulSoup
import urlparse
import re

class htmlParser(object):
    def parser(self, page_url, html):
        '''
        解析html
        :param page_url:要解析的页面url地址
        :param html: 要解析的页面的代码
        :return:
        '''
        if page_url is None or html is None:
            return
        soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
        # 调用get_datas解析当前页面的所有数据
        datas = self.get_datas(page_url, soup)
        # 调用get_urls解析当前页面的关联地址
        urls = self.get_urls(page_url, soup)

        return {'urls':urls,'datas':datas}

    def get_datas(self,page_url,soup):
        '''
        解析出当前页面所需要的数据
        :param page_url:要解析的页面url地址
        :param html: 要解析的页面的代码
        :return:
        '''
        #定义一个字典存储当前页的数据
        try:
            datas={}
            datas['url']=page_url
            h1=soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
            datas['title']=h1.string
            div=soup.find("div",class_="lemma-summary")
            datas['msg']=div.get_text()
            print datas
            return datas
        except:
            pass

    #https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB
    def get_urls(self,page_url,soup):
        '''
        解析出当前页面所有关联的url
        :param page_url:要解析的页面url地址
        :param html: 要解析的页面的代码
        :return:
        '''
        #定义一个set集合存储所有的新的url
        new_urls=set()
        a_s=soup.find_all("a",href=re.compile("/item/.+"))
        for a in a_s:
            href=a['href']
            full_url=urlparse.urljoin(page_url,href)
            new_urls.add(full_url)
            print full_url
        return new_urls
