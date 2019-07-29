#coding:utf-8
import scrapy
from qq.items import QqItem
from scrapy.selector import Selector

#写一个爬虫类，爬虫类要继承scrapy.Spider
class blogSpider(scrapy.Spider):
	#爬虫的名字
	name="blog"
	#允许的域名
	allow_domains=["cnblogs.com"]
	#根url
	start_urls=["http://www.cnblogs.com/qiyeboy/default.html?page=1"]

	#解析数据
	def parse(self,response):
		#提取数据
		days=response.xpath("//*[@class='day']")
		for day in days:
			time=day.xpath("./div[@class='dayTitle']/a/text()").extract()[0]
			title=day.xpath("./div[@class='postTitle']/a/text()").extract()[0]
			#获取文章连接
			href=day.xpath("./div[@class='postTitle']/a/@href").extract()[0]
			#获取摘要
			content=day.xpath("./div[@class='postCon']/div/text()").extract()[0]
			#{"time":time,"title":title,"href":href,"content":content}
			#创建一个Item对象
			#print time,title,href,content
			print time
			qqItem=QqItem(time=time,href=href,content=content,title=title)
			#请求文章详细信息页面
			request=scrapy.Request(url=href,callback=self.parse_body)
			request.meta['item']=qqItem;
			yield request

		#翻页提取
		#创建一个选择器对象
		nextPage=Selector(response).re(u'<a href="(\S*)">下一页</a>') 
		#判断是否有下一页
		if nextPage:
			yield scrapy.Request(url=nextPage[0],callback=self.parse)
	
			
	#解析正文的函数
	def parse_body(self,response):
		#获取页面上class=‘postBody’
		body=response.xpath("//*[@class='postBody']")
		#从正文中获取所有图片的src属性
		image_urls=body.xpath(".//img//@src").extract()
		#获取qqItem
		qqItem=response.meta['item']
		qqItem['image_urls']=image_urls
		yield qqItem
