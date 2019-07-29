#coding:utf-8
from multiprocessing.managers import BaseManager
from HTMLDownloader import htmlDownloader
from HTMLParser import htmlParser

class Main(object):
	def __init__():
		BaseManager.register('get_url_q')
		BaseManager.register('get_result_q')
		self.m=BaseManager(address=('127.0.0.1',8001),authkey="baike")
		#获取连接
		self.m.connect()
		self.url_q=self.m.get_url_q()
		self.result_q=self.m.get_result_q()
		self.down=htmlDownloader()
		self.parser=htmlParser()
		
	def action(self):
		if not self.url_q.empty():
			#从队列中获取一个要下载的url地址
			new_url=self.url_q.get()
			if new_url=='over':
				print "任务结束"
				self.result_q.put({'urls:':'over','datas':'over'})
				return
			#调用html下载器下载数据
			html=self.down.download(url)
			#调用html解析器解析数据
			dic=self.parser.parser(new_url,html)
			#把返回的数据存储到result_q队列中
			self.result_q.put(dic)
			
