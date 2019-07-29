# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem

class QqPipeline(object):

	def __init__(self):
		self.file=open("blog.json",'w')

	#把item存储到一个json文件中
	def process_item(self, item, spider):
		if item['title']:
			jsonStr=json.dumps(dict(item))
			self.file.write(jsonStr)
			return item
		else:
			#抛出一个异常
			raise DropItem("%s丢失了title"%str(item))
