#coding:utf-8
from multiprocessing.managers import BaseManager
from HTMLDownloader import htmlDownloader
from aa import htmlParser

class ww(object):
	def __init__(self):
		BaseManager.register('get_url_q')
		BaseManager.register('get_result_q')
		self.m=BaseManager(address=('192.168.32.130',8001),authkey="baike")
		#获取连接
		self.m.connect()
		print "连接成功"
		self.url_q=self.m.get_url_q()
		self.result=self.m.get_result_q()
		self.down=htmlDownloader()
		self.par=htmlParser()

	def action(self):
		while True:
			if not self.url_q.empty():
				#从队列中获取一个要下载的url地址
				new_url=self.url_q.get()
				if new_url=='over':
					print "任务结束"
					self.result.put({'urls:':'over','datas':'over'})
					return
				#调用html下载器下载数据
				html=self.down.download(new_url)
				print html
				#调用html解析器解析数据
				dic=self.par.parser(new_url,html)
				# 把返回的数据存储到result_q队列中
				self.result.put(dic)

			

if __name__=='__main__':
	w=ww()
	w.action()