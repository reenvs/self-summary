# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from qq.items import QqItem

#爬取公务员题库
class HelloSpider(scrapy.Spider):
    name = "hello"
    allowed_domains = ["chinagwy.org"]
    start_urls = (
        'http://www.chinagwy.org/html/stzx/201603/7_143757.html',
    )

    def parse(self, response):
	table=response.xpath("//*[@id='table1']")
	hrefs=table.xpath(".//a/@href").extract()
	for href in hrefs:
		helloItem=QqItem()
		request=scrapy.Request(url=href,callback=self.parse_body)
		request.meta['item']=helloItem
		yield request

    def parse_body(self,response):
	urls=Selector(response).re(u'<a href="(\S*?doc[x]{0,1})"') 
	if len(urls)!=0:
		item=response.meta['item']	
		item['file_urls']=urls
		print '*'*20
		yield item

